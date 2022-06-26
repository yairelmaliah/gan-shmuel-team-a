from http.client import OK
import mimetypes
from sqlite3 import IntegrityError
from urllib import response
import requests
from flask import Flask, render_template, request
import json
from db_utils import db_utils


my_sql = db_utils()

def id_check(where,what):
    id_check = my_sql.getData(f'SELECT EXISTS(SELECT * FROM {what} WHERE id="{where}");')
    y = json.dumps(id_check)
    value_id = str(y[-3])
    return value_id


def PUT_truck(truck_id):

    license_plate = str(truck_id)
    provider_id = request.form['provider_id']
    

    if id_check(what="Trucks",where=license_plate) != str(1):
        return (f"your truck id : {license_plate} is not exist! please try again.", 409)

    elif id_check(what="Provider",where=provider_id) == str(0):
        return (f"your provider id : {provider_id} is not exist! please try again." , 409)

    else:
        my_sql.updateData(f'UPDATE `Trucks` SET provider_id = {provider_id} WHERE id = "{license_plate}";')
        return(f"Enjoy! your  license plate : {license_plate} changed provider id to {provider_id}!", 200)


if __name__ == '__main__':
    PUT_truck()    
