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
    id_check = my_sql.getData(f'SELECT EXISTS(SELECT * FROM `Trucks` WHERE id="{license_plate}");')
    dump = json.dumps(id_check)
    value = str(dump[-3])
    
    if value == str(0):
        return (f"License plate : {license_plate} is not exist!, please try again.", 404)

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
   # http://localhost:8081/get_item/10006
 #   try :
  #  sleep (2)

    # i=0
    # not_found=True
    # while i < 30 and not_found:
    #     try:
   


    data = request.get_json("http://3.66.68.27:8080/api/provider")


    return jsonify({'you sent ':data})

    dump = json.dumps(res)
    data = json.loads(dump)
    return str(data)
    #         not_found = False
    #  #   ba = "laal"
    #     except ConnectionError:
    #         sleep(2)
    #         i += 1

    

   # return res
    

if __name__ == '__main__':
    GET_truck(id)    
