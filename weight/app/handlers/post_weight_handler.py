from db import Mysql
import time
import json
from flask import abort
mysql = Mysql()

directions_to_use = { "in","out","none"}
weight_unit_to_use = {"kg","lbs"}

def check_syntax(direction, weight_unit):
    if direction not in directions_to_use:
        abort(400, "direction {} doesn't exist".format(direction))

    if weight_unit not in weight_unit_to_use:
        abort(400, "weight unit {} doesn't exist".format(weight_unit))

def post_weight_handler(args):

  direction = args.get('direction', None)
  truck = args.get('truck', None)
  containers = args.get('containers',None)
  weight = args.get('weight',None)
  unit = args.get('unit', "kg")
  force = args.get('force', "false")
  produce = args.get('produce', None)

  if not weight:
    abort(400, "must insert weight")

  if not containers and not truck:
    abort(400, "must insert truck license plate or container id")

  check_syntax(direction, unit)

  time_now = time.strftime('%Y%m%d%H%M%S')
  print(time_now, flush=True)
  # Check if theres already a truck/container session
  query = f"SELECT id,direction FROM `transactions` WHERE truck = {truck} order by datetime desc limit 1"
  exist_session = mysql.get_data(query)

  if exist_session and exist_session[0][1] == direction:
    
    if force == "false": abort(400, f"Error in direction -> caused by {truck}")

    if force == "true":
      if direction == "in":
        return update_in_session(exist_session[0][0], time_now, truck, containers, weight, produce)
      if direction == "out":
        return update_out_sessions(exist_session[0][0], time_now, truck, containers, weight, produce)


  if direction == "in" or direction == "none":
    check_if_container_exist_and_insert(containers)
    return insert_in_session(time_now, truck, containers, weight, produce)

  if direction == "out":
    return insert_out_session(time_now, truck, containers, weight, produce)
  return "SUCCESS"

def check_if_container_exist_and_insert(containers):
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
  transaction_data = mysql.get_data(f'SELECT bruto,containers,produce from transactions WHERE truck = {truck} order by datetime desc limit 1')
  containers = transaction_data[0][1].split(",")
  bruto = transaction_data[0][0]
  produce = transaction_data[0][2]
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

  query = """INSERT INTO transactions (datetime, direction, truck, containers, bruto, truckTara ,neto,produce)
              VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""

  data = (time, "out", truck, ",".join(containers),bruto, weight, neto, produce)

  mysql.insert_data(query,data)
  session_id = mysql.get_data(f'SELECT id from transactions WHERE truck = {truck} order by datetime desc limit 1')
  session_id = session_id[0][0]

  return json.dumps({ "id": session_id, "truck": truck,"bruto": bruto,"truckTara": weight, "neto": neto })


def update_out_sessions(id, time, truck, containers,weight, produce):
  transaction_data = mysql.get_data(f'SELECT bruto,containers from transactions WHERE truck = {truck} AND direction = "in"')
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
  return json.dumps({ "id": get_new_session_id(id), "truck": truck,"bruto": bruto,"truckTara": weight, "neto": neto })
  
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
  mysql.update_data(query, (time, "in", truck, containers, weight, produce,))
  return json.dumps({ "id": get_new_session_id(id), "truck": truck,"bruto": weight })

def insert_in_session(time, truck, containers, weight, produce):
  query = """
        INSERT INTO transactions 
        (datetime, direction, truck, containers, bruto,produce) VALUES (%s,%s,%s,%s,%s,%s)
        """
  data = (time, "in", truck, ",".join(containers), weight, produce)
  mysql.insert_data(query, data)

  session_id = mysql.get_data(f'SELECT id from transactions WHERE truck = {truck} order by datetime desc limit 1')
  session_id = session_id[0][0]
  # request.post()
  return json.dumps({ "id": session_id, "truck": truck,"bruto": weight })


def get_new_session_id(_id):
  session_id = mysql.get_data(f'SELECT `id` from transactions WHERE `id` = {_id}')
  session_id = session_id[0][0]
  return session_id