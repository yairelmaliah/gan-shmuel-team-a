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

    try:
        from_date = request.args['from']
        to_date = request.args['to']

        if from_date > to_date:
            return("from date is larger than to date. please try again.", 409)

        if len(from_date) != 14 or from_date.isnumeric() == False:
            return (f"from_date is not valid, please try again.", 409)

        elif len(to_date) != 14 or to_date.isnumeric() == False:
            return (f"to_date is not valid, please try again.", 409)

    except werkzeug.exceptions.BadRequestKeyError:

        from_date = currentDT.strftime("%Y%m01000000")
        to_date = currentDT.strftime("%Y%m%d%H%M%S")

    
    is_exists = my_sql.getData(f"SELECT EXISTS(SELECT provider_id FROM Trucks WHERE id='{license_plate}');")
    dump = json.dumps(is_exists)
    value = str(dump[-3])
    
    if value == str(0):
        return (f"License plate: {license_plate} does not exists, please try again.", 404)


    provider_id_check = my_sql.getData(f"SELECT provider_id FROM Trucks WHERE id='{license_plate}';")
    dump = json.dumps(provider_id_check)
    load = json.loads(dump)
    provider_id = str(load[0]['provider_id'])

    data = requests.get(f"http://3.66.68.27:8081/item/{license_plate}?from'{from_date}'to'{to_date}'").json()
    data['id'] = provider_id


    return data


if __name__ == '__main__':
    GET_truck(id)    
