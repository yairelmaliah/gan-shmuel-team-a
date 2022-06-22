from db import Mysql
from datetime import datetime
import json

def get_item_handler(args,_id):
  mysql = Mysql()
  fromTime = args.get('from') if args.get('from') else datetime.now().strftime("%Y%m%d000000")
  toTime = args.get('to') if args.get('to') else datetime.now().strftime("%Y%m%d%H%M%S")

  if _id.isdigit():
    query = """SELECT * FROM transactions WHERE transactions.datetime BETWEEN '{0}' AND '{1}' AND truck = '{2}'"""
  
  else:
    query = """
    SELECT * FROM transactions WHERE datetime BETWEEN '{0}' AND '{1}'
    AND containers LIKE '%{2}%'"""
  
  info = mysql.get_data(query.format(fromTime, toTime, _id))

  if info:
    return json.dumps({
      "id": _id,
      "tara": info[-1][6],
      "transactions": [x[0] for x in info]
    })
  
  return f"There is no such container/truck with this id {_id} :("
  