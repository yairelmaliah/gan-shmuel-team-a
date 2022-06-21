from http.client import OK
import mimetypes
from sqlite3 import IntegrityError
from urllib import response
import requests
from flask import Flask, render_template, request
import json
from db_utils import db_utils


my_sql = db_utils()

def id_check(where):
    id_check = my_sql.getData(f'SELECT EXISTS(SELECT * FROM Trucks WHERE id="{where}");')
    y = json.dumps(id_check)
    value_id = str(y[-3])
    return value_id


def PUT_truck(id):

    license_plate = str(id)
    new_id = request.args['provider_id']
    


    if id_check(license_plate) != str(1):
        return (f"your truck id : {license_plate} is not exist! please try again.", 409)

    else:
        my_sql.updateData(f'UPDATE `Trucks` SET provider_id = {new_id} WHERE id = "{license_plate}";')
        return(f"Enjoy! your  license plate : {license_plate} changed provider id to {new_id}!", 200)


if __name__ == '__main__':
    PUT_truck()    
