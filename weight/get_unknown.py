from db import Mysql

def get_unknown():
	mySQL = mysql_db()

	try:
		info = mySQL.getData("SELECT distinct id FROM containers WHERE weight IS NULL")		
		if len(info) == 0:
			return "No missing weights found in data base"
		return '\n'.join(map(str,info))
		
	except:		
		return "Weight data is unavailable at the moment."
