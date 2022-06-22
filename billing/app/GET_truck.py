from http.client import OK
import mimetypes
from sqlite3 import IntegrityError
from urllib import response
import requests
from flask import Flask, render_template, request
import json
from db_utils import db_utils

my_sql = db_utils()



def GET_truck(id):

    return "OK"
    provider_id = str(id)
    id = my_sql.getData(f'SELECT EXISTS(SELECT * FROM Provider WHERE id="{provider_id}");')
    x = json.dumps(id)
    value = str(x[-3])

    if value == str(0):
        return (f"Provider id : {provider_id} not found, please try again.", 404)
    
   
        


if __name__ == '__main__':
    GET_truck()    
