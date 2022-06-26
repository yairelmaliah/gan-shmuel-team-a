from db import Mysql
import time

mysql = Mysql()

directions_to_use = { "in","out","none"}
weight_unit_to_use = {"kg","lbs"}

def check_syntax(direction, weight_unit):
    if direction not in directions_to_use:
        return {"data": "direction {} doesn't exist".format(direction)}, 400


    if weight_unit not in weight_unit_to_use:
        return {"data": "weight unit {} doesn't exist".format(weight_unit)},400

def post_weight_handler(args):

  direction = args.get('direction', None)
  truck = args.get('truck', None)
  containers = args.get('containers',None)
  weight = args.get('weight',None)
  unit = args.get('unit', "kg")
  force = args.get('force', "false")
  produce = args.get('produce', None)

  if not weight:
    return {"data":"must insert weight"}, 400

  if not containers and not truck:
    return {"data":"must insert truck license plate or container id"}, 400

  check_syntax(direction, unit)

  time_now = time.strftime('%Y%m%d%H%M%S')

  query = f"SELECT id,direction FROM `transactions` WHERE truck = '{truck}' order by datetime desc limit 1"
  exist_session = mysql.get_data(query)
  
  if exist_session and exist_session[0][1] == "in" and direction == "none":
    return {"data": f"Not possible to insert none after in -> caused by {truck}"},400

  if exist_session and exist_session[0][1] == direction:

    if force == "false": return {"data":f"Error in direction -> caused by {truck}"}, 400

    if force == "true":
      if direction == "in":
        return update_in_session(exist_session[0][0], time_now, truck, containers, weight, produce)
      if direction == "out":
        return update_out_sessions(exist_session[0][0], time_now, truck, containers, weight, produce)


  if direction == "in" or direction == "none":
    check_if_container_exist_and_insert(containers)
    return insert_in_session(time_now, direction, truck, containers, weight, produce)

  if direction == "out":
    if check_if_truck_exist(truck):
        return insert_out_session(time_now, truck, containers, weight, produce)
    return {"data": f"truck {truck} never entered Gan Shmouel"},400

def check_if_truck_exist(truck):
  query = f"""
          SELECT * from transactions WHERE truck = '{truck}'"""
  data = mysql.get_data(query)
  query1 = f"""
          SELECT direction from transactions WHERE truck = '{truck}' ORDER BY id DESC LIMIT 1"""
  data1 = mysql.get_data(query1)  
  
  
  if not data or data1[0][0] == "none":
    return False
  return True



def check_if_container_exist_and_insert(containers):
  
  containers= containers.split(",")
  
  for container in containers:
    query = f"""
            SELECT * from containers_registered WHERE container_id = "{container}"
            """
    data = mysql.get_data(query)
    
    if not data:
      query = """INSERT IGNORE INTO containers_registered (container_id) VALUES (%s)"""
      data = (container,)
      mysql.insert_data(query, data)



def insert_out_session(time, truck, containers , weight, produce):
  transaction_data = mysql.get_data(f"""SELECT bruto,containers,produce from transactions WHERE truck = '{truck}' order by datetime desc limit 1""")
  containers = transaction_data[0][1].split(",")
  bruto = transaction_data[0][0]
  produce = transaction_data[0][2]
  total_containers_weight = 0
  flag=False

  for container in containers:
    query = f"""
            SELECT weight from containers_registered WHERE container_id = "{container}"
              """ 
    cont_data = mysql.get_data(query)
    
    if cont_data[0][0] != None:

      if cont_data[0][0]:
        total_containers_weight += cont_data[0][0]
    else:
      flag=True
      
  if not flag:
    neto = bruto - total_containers_weight - int(weight)
  else:
    neto=None

  query = """INSERT INTO transactions (datetime, direction, truck, containers, bruto, truckTara , neto, produce)
              VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""

  data = (time, "out", truck, ",".join(containers),bruto, weight, neto, produce)

  mysql.insert_data(query,data)
  session_id = mysql.get_data(f"""SELECT id from transactions WHERE truck = '{truck}' order by datetime desc limit 1""")
  session_id = session_id[0][0]

  return { "id": session_id, "truck": truck,"bruto": bruto,"truckTara": weight, "neto": neto }, 200


def update_out_sessions(id, time, truck, containers,weight, produce):
  transaction_data = mysql.get_data(f'SELECT bruto,containers from transactions WHERE truck = "{truck}" AND direction = "in"')
  containers = transaction_data[0][1].split(",")
  bruto = transaction_data[0][0]
  total_containers_weight = 0
  
  for container in containers:
    query = f"""
            SELECT weight from containers_registered WHERE container_id = "{container}"
            """
    cont_data = mysql.get_data(query)
    if cont_data:
      if cont_data[0][0]:
        total_containers_weight += cont_data[0][0]

  neto = bruto - total_containers_weight - int(weight)

  query = """
          UPDATE transactions 
          SET 
          datetime = %s,
          truck = %s,
          direction = %s,
          containers = %s,
          bruto = %s,
          truckTara = %s,
          neto = %s,
          produce = %s
          WHERE `id` = %s
          """

  mysql.update_data(query, (time,truck,"out", ",".join(containers), bruto, weight,neto,produce,id,))
  return { "id": get_new_session_id(id), "truck": truck,"bruto": bruto,"truckTara": weight, "neto": neto }, 200
  
def update_in_session(id, time, truck, containers, weight, produce):
  query = """
        UPDATE transactions 
        SET 
        datetime = %s,
        direction = %s,
        truck = %s,
        containers = %s,
        bruto = %s,
        produce = %s
        WHERE `id` = %s
        """
  mysql.update_data(query, (time, "in", truck, containers, weight, produce,id))
  return { "id": get_new_session_id(id), "truck": truck,"bruto": weight }, 200

def insert_in_session(time, direction, truck, containers, weight, produce):
  
  query = """
        INSERT INTO transactions 
        (datetime, direction, truck, containers, bruto, produce) VALUES (%s,%s,%s,%s,%s,%s)
        """
  containers = containers.split(",")
  data = (time, direction, truck, ",".join(containers), weight, produce)
  mysql.insert_data(query, data)
  session_id = mysql.get_data(f'SELECT id from transactions WHERE truck = "{truck}" order by datetime desc limit 1')
  session_id = session_id[0][0]
  # request.post()
  return { "id": session_id, "truck": truck,"bruto": weight }, 200


def get_new_session_id(_id):
  session_id = mysql.get_data(f'SELECT `id` from transactions WHERE `id` = {_id}')
  session_id = session_id[0][0]
  return session_id




  #",".join(containers)