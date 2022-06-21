from flask import Flask, render_template, request, redirect
import json
from db_utils import db_utils


mysql = db_utils()

def data_exist():
    new_provider = request.args['new_provider']
    name = mysql.getData(f"SELECT * from Provider WHERE name=('{new_provider}')")
    json_str = json.dumps(name)
    resp = json.loads(json_str)
    return resp[0]['name']

def update_new_provider(id):
    new_provider = request.args['new_provider']
    provider_id = id
    new_name = f"UPDATE Provider SET name = ('{new_provider}') WHERE id = ('{provider_id}');"
    mysql.updateData(new_name)
    return f"Provider name changed, Id: {id}"



def PUT_provider(id):
    try:
        if not data_exist():
            return update_new_provider(id), 200 # does not exist
        return f"Provider name already exist", 409 # exist
    except:
        return update_new_provider(id), 200 # does not exist


if __name__ == '__main__':
    PUT_provider()
