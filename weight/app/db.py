import mysql.connector
import os

class Mysql():
  def __init__(self):
    if not os.environ.get("TEST_DB",None):
      self.host = "sql"
    else: 
      self.host = "sql_test"

    self.user="root",
    self.password="1234",
    self.database="weight"
    self.connected = None

  def connect_to_db(self):
    if self.connected is None:
      self.connected = mysql.connector.connect(host=self.host,user="root",password="1234",database="weight")
    return self.connected

  def insert_data(self,query, data):
    connected = self.connect_to_db()
    mycursor = connected.cursor()
    mycursor.execute(query, data)
    connected.commit()
	
  def update_data(self, query, data=None):
    connected = self.connect_to_db()
    mycursor = connected.cursor()
    mycursor.execute(query, data)
    connected.commit()

  def get_data(self, query):
    connected = self.connect_to_db()
    mycursor = connected.cursor()
    mycursor.execute(query)
    results = mycursor.fetchall()
    return results