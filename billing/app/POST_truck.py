import requests
from flask import Flask, render_template, request
import json
from db_utils import db_utils


mysql = db_utils()



def POST_truck():

    id_number = "10001"
    provider = "something"
    #data_insert = f"INSERT INTO Provider (name) VALUES ('{provider}');"

    id = mysql.getData("SELECT EXISTS(SELECT * FROM Provider WHERE id=10000);")
    #mysql.setData(data_insert)
    # return mysql.getData(f'select name,id from Provider where name = "{val}"')
    return json.dumps(id)
    


if __name__ == '__main__':
    POST_truck()    
