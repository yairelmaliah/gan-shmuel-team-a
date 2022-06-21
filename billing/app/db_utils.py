from unittest import result
import mysql.connector

class db_utils(object):
	def __init__(self):
		self.db_user = "root"
		self.db_pass = "12345"
		self.db_host = "billing_db"
		self.db_name = "billdb"
		self.connections = None

	def doConnect(self):
		if self.connections is None:
			self.connections = mysql.connector.connect(user='root', password='12345', host='billing_db', database='billdb')
		return self.connections

	def getData(self,query):
		connected = self.doConnect()
		cur = connected.cursor(dictionary=True, buffered=True)
		cur.execute(query)
		results = cur.fetchall()
		return results

	def setData(self, query):
		connected = self.doConnect()
		cursor = connected.cursor()
		cursor.execute(query)
		connected.commit()
  
	def updateData(self, query):
		connected = self.doConnect()
		cursor = connected.cursor()
		cursor.execute(query)
		connected.commit()
	
	# def checker(self):
	# 	connected = self.doConnect()
	# 	cur = connected.cursor(dictionary=True, buffered=True)
	# 	results = cur.fetchall()
	# 	return results
