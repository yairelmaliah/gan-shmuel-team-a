from http.client import BAD_REQUEST, OK
import mimetypes
from sqlite3 import IntegrityError
from urllib import response
import requests
from flask import Flask, render_template, request
import json
from db_utils import db_utils
import datetime
import werkzeug
my_sql = db_utils()



 


def GET_truck(id):

    currentDT = datetime.datetime.now()


    license_plate = str(id)
  
    id_check = my_sql.getData(f'SELECT EXISTS(SELECT * FROM `Trucks` WHERE id="{license_plate}");')
    dump = json.dumps(id_check)
    value = str(dump[-3])

    if value == str(0):
        return (f"Provider id : {license_plate} is not exist!, please try again.", 404)

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


   



    return (f"test : {from_date}")
    

if __name__ == '__main__':
    GET_truck()    
