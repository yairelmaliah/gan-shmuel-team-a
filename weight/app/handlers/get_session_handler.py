from db import Mysql

def get_session_handler(id):
  mysql = Mysql()
  session = mysql.get_data(f"SELECT * from transactions WHERE id={id} order by datetime desc limit 1")
  if not session:
    return {"data": "Invalid session ID"}, 404

  if session[0][2] == 'out':
    return {
          "id": id,
          "direction": session[0][2],
          "truck": session[0][3],
          "bruto": session[0][5],
          "truckTara": session[0][6],
          "neto": session[0][7],
          "produce":session[0][8]
          }, 200

  else:
    return {
      "id": id,
      "direction": session[0][2],
      "truck": session[0][3],
      "bruto": session[0][5],
      "produce":session[0][8]
    }, 200

