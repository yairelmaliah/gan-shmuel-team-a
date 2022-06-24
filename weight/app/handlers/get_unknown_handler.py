from db import Mysql

def get_unknown_handler():
	mysql = Mysql()

	data = mysql.get_data("SELECT distinct container_id FROM containers_registered WHERE weight IS NULL")
	if not data:
		return "There are no containers without weight :)", 200
	return {"data":[x[0] for x in data]}, 200
		