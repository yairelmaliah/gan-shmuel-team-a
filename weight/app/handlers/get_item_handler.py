from db import Mysql
from datetime import datetime

def get_item_handler(args,_id):
  mysql = Mysql()
  fromTime = args.get('from') if args.get('from') else datetime.now().strftime("%Y%m01000000")
  toTime = args.get('to') if args.get('to') else datetime.now().strftime("%Y%m%d%H%M%S")

  fromTime = '{:<14d}'.format(int(fromTime))
  toTime = '{:<14d}'.format(int(toTime))


  query = "select * from transactions order by datetime desc"
  data = mysql.get_data(query)

  arr = []
  for trans in data:
    time = int(trans[1].strftime('%Y%m%d%H%M%S'))
    if _id in trans and int(fromTime) < time < int(toTime):
      arr.append(trans)

  if arr:
    return {
      "id": _id,
      "tara": arr[0][6],
      "sessions": [s[0] for s in arr]
    }, 200
  
  return {"data": f"There is no such container/truck with this id '{_id}'"}, 404
