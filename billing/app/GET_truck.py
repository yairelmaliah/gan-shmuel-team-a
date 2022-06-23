from http.client import BAD_REQUEST, OK
import mimetypes
from sqlite3 import IntegrityError
from unicodedata import east_asian_width
from urllib import response
import requests
from flask import Flask, render_template, request
import json
from db_utils import db_utils
import datetime
import werkzeug
from time import sleep
from requests import Session
from requests.adapters import HTTPAdapter
#from requests.packages.urllib3.util.retry import Retry
from requests.exceptions import ConnectionError
from flask import jsonify

my_sql = db_utils()


   
def GET_truck(id):

    currentDT = datetime.datetime.now()
    license_plate = str(id)
    # id_check = my_sql.getData(f'SELECT EXISTS(SELECT * FROM `Trucks` WHERE id="{license_plate}");')
    # dump = json.dumps(id_check)
    # value = str(dump[-3])
    
    # if value == str(0):
    #     return (f"License plate : {license_plate} is not exist!, please try again.", 404)

    try:
        from_date = request.args['from']
        to_date = request.args['to']
        if len(from_date) != 14 or from_date.isnumeric() == False:
            return (f"from_date is not valid, please try again.", 409)

        elif len(to_date) != 14 or from_date.isnumeric() == False:
            return ("to_date is not valid, please try again.", 409)

    except werkzeug.exceptions.BadRequestKeyError:

        from_date = currentDT.strftime("%Y%m01000000")
        to_date = currentDT.strftime("%Y%m%d%H%M%S")

     #localhost:8080/truck/135-43-132?from=20220311 203010&to=20220312 203010

    provider_id_check = my_sql.getData(f"SELECT provider_id FROM Trucks WHERE id='{license_plate}';")
    provider_id = str(provider_id_check[0]['provider_id'])
    return provider_id

   # data = requests.get(f"http://3.66.68.27:8081/item/'{license_plate}'?from'{from_date}'to'{to_date}'").json()

   # new_data = data['id'] = provider_id
   

   # return new_data
    

if __name__ == '__main__':
    GET_truck(id)    
