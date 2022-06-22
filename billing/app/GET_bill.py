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
from requests import Session
from requests.adapters import HTTPAdapter
#from requests.packages.urllib3.util.retry import Retry
from requests.exceptions import ConnectionError



my_sql = db_utils()

   
def GET_bill(id):

    currentDT = datetime.datetime.now()
    provider_id = str(id)
  
    id_check = my_sql.getData(f'SELECT EXISTS(SELECT * FROM `Provider` WHERE id="{provider_id}");')
    dump = json.dumps(id_check)
    value = str(dump[-3])

    if value == str(0):
        return (f"Provider id : {provider_id} is not exist!, please try again.", 404)

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




    return "OK"
    

if __name__ == '__main__':
    GET_bill()    
