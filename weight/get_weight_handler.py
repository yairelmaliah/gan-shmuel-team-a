from db import Mysql
from datetime import datetime

def get_weight_handler(args):
  mysql = Mysql()
  fromTime = args.get('from') if args.get('from') else datetime.now().strftime("%Y%m%d000000")
  toTime = args.get('to') if args.get('to') else datetime.now().strftime("%Y%m%d%H%M%S")
  filter_directions = f"('{args.get('filter')}')" if args.get('filter') else "('in', 'out', 'none')" 
  query="""SELECT id, direction,containers, bruto, neto, produce
      FROM transactions 
      WHERE transactions.datetime BETWEEN  '{0}' AND '{1}'
      AND direction IN {2}"""
  info = mysql.get_data(query.format(fromTime, toTime, filter_directions))	
      
  return str(info)
