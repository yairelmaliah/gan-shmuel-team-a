from flask import Flask, render_template, request
import json
from db_utils import db_utils


mysql = db_utils()

def data_exist():
    provider_name = request.form['provider']
    name = mysql.getData(f"SELECT * from Provider WHERE name=('{provider_name}')")
    json_str = json.dumps(name)
    resp = json.loads(json_str)
    return resp[0]['name']

def push_new_provider():
    provider = request.form['provider']
    data_insert = f"INSERT INTO Provider (name) VALUES ('{provider}');"
    mysql.setData(data_insert)
    id = mysql.getData("SELECT id FROM Provider ORDER BY id DESC LIMIT 1;")
    return json.dumps(id)

def POST_provider():
    try:
        if not data_exist():
            return push_new_provider(), 200 # does not exist, push new one!
        return "Provider name already exist", 409 # exist, not allowed to push
    except:
        return push_new_provider(), 200 # does not exist, push new one!

if __name__ == '__main__':
    POST_provider()
    data_exist()
