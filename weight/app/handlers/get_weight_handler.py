from db import Mysql
from datetime import datetime

def get_weight_handler(args):
  mysql = Mysql()
  fromTime = args.get('from') if args.get('from') else datetime.now().strftime("%Y%m%d000000")
  toTime = args.get('to') if args.get('to') else datetime.now().strftime("%Y%m%d%H%M%S")
  filter_directions = f"('{args.get('filter')}')" if args.get('filter') else "('in', 'out', 'none')"

  fromTime = '{:<14d}'.format(int(fromTime))
  toTime = '{:<14d}'.format(int(toTime))

  query = "select id,datetime, direction,containers, bruto, neto, produce from transactions order by datetime desc"
  data = mysql.get_data(query)
  arr = []

  for trans in data:
    time = int(trans[1].strftime('%Y%m%d%H%M%S'))
    if int(fromTime) < time < int(toTime):
      arr.append({
        "id": trans[0],
        "direction": trans[2],
        "bruto": trans[4],
        "neto": trans[5],
        "produce": trans[6],
        "containers": trans[3].split(',') if trans[3] else None,
      })

  if not arr:
    return "There is No weight at the moment" , 404

  return {"data" : arr}, 200
