from db import Mysql
import time
import json

mysql = Mysql()

def post_weight_handler(args):
  direction = args.get('direction')
  truck = args.get('truck')
  containers = args.get('containers').split(",")
  weight = int(args.get('weight'))
  unit = args.get('unit')
  force = args.get('force')
  produce = args.get('produce')

  already_updated = False

  time_now = time.strftime('%Y%m%d%H%M%S')

  total_containers_weight = 0

  for container in containers:
    query = f"""
            SELECT weight from containers_registered WHERE container_id = "{container}"
            """
    total_containers_weight += mysql.get_data(query)[0][0]

  # ==========================================
  # Check if truck has an already session on database
  query = f"SELECT id,direction FROM `transactions` WHERE truck = {truck} order by datetime desc limit 1"
  last_direction = mysql.get_data(query)

  # If truck direction same as the last one
  if last_direction:
    if last_direction[0][1] == direction:
      if force == "true":
        if direction == "in":
          mysql.update_data(f'UPDATE transactions SET bruto = {weight} WHERE id = {last_direction[0][0]}')
          already_updated = True
      else:
        return f'Error in direction -> caused by {truck}'

  # if its the first time truck is entering
  if direction == 'in' or direction == 'none':
    if not already_updated:
      query = """
              INSERT INTO transactions 
              (datetime, direction, truck, containers, bruto,produce) VALUES (%s,%s,%s,%s,%s,%s)
          """
      data = (time_now, "in", truck, ",".join(containers), weight, produce)
      mysql.insert_data(query, data)

    session_id = mysql.get_data(f'SELECT id from transactions WHERE truck = {truck} order by datetime desc limit 1')
    session_id = session_id[0][0]

    return json.dumps({ "id": session_id, "truck": truck,"bruto": weight })

  if direction == 'out':
    # bruto - c_weight - t_weight
    transaction_data = mysql.get_data(f'SELECT bruto,containers from transactions WHERE truck = {truck}')
    containers = transaction_data[0][1].split(",")
    bruto = transaction_data[0][0]
    total_containers_weight = 0
    for container in containers:
      query = f"""
              SELECT weight from containers_registered WHERE container_id = "{container}"
              """
      total_containers_weight += mysql.get_data(query)[0][0]

    neto = bruto - total_containers_weight - weight
    mysql.update_data(f'UPDATE transactions SET neto = {neto},truckTara = {weight}, direction = "out"  WHERE truck = {truck}')
    session_id = mysql.get_data(f'SELECT id from transactions WHERE truck = {truck} order by datetime desc limit 1')
    session_id = session_id[0][0]

    return json.dumps({ "id": session_id, "truck": truck,"bruto": bruto,"truckTara": weight, "neto": neto })

  return "Something went wrong :("




