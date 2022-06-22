from db import Mysql

def get_unknown_handler():
	mysql = Mysql()

	try:
		data = mysql.get_data("SELECT distinct container_id FROM containers_registered WHERE weight IS NULL")
		if not data:
			return "There are no containers without weight :)", 200
		return '\n'.join(map(str,data))
		
	except:		
		return "Weight data is unavailable at the moment."

