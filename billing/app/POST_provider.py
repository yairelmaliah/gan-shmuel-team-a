import requests
from flask import Flask, render_template, request
import json
from db_utils import db_utils


mysql = db_utils()



def POST_provider():
    # val = "test2"
    provider = request.form['provider']
    data_insert = f"INSERT INTO Provider (name) VALUES ('{provider}');"
    id = mysql.getData("SELECT id FROM Provider ORDER BY id DESC LIMIT 1;")

    mysql.setData(data_insert)
    # return mysql.getData(f'select name,id from Provider where name = "{val}"')
    return json.dumps(id)
    


if __name__ == '__main__':
    POST_provider()    
