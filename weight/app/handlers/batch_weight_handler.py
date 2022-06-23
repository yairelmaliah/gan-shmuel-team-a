from db import Mysql
import os
import csv

def batch_weight_handler(file):
  mysql = Mysql()
  query = """INSERT IGNORE INTO containers_registered (container_id, weight, unit) VALUES (%s,%s,%s)"""
  
  try:
    if file in os.listdir("in/"):
      
      if ".csv" in file:
        with open(f"in/{file}", "r") as f:
          reader = list(csv.reader(f))
          unit = reader[0][1]

          for row in reader[1:]:
            container_id = row[0]
            try:
              weight = int(row[1]) 
            except:
              weight = ''
            data = (container_id, weight, unit)
            mysql.insert_data(query, data)
        return f"{file} Has Been Added To Database Succesfully", 200

      elif ".json" in file:
        import json
        with open(f"in/{file}", "r") as f:
          data = json.load(f)      
          for i in data:
            container_id = i["id"]
            try:
              weight = int(i["weight"])
            except:
              weight = ''
            data = (container_id, weight, i["unit"])
            mysql.insert_data(query, data)
    
        return f"{file} Has Been Added To Database Succesfully", 200

  except Exception as e:
    return f"Can't load this file '{file}' , Please check the file"

  return f"Sorry, but {file} doe's not exist", 404


