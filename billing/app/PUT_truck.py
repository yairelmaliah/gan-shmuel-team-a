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

def PUT_truck():

    license_plate = '134-33-443'
    new_license_plate = '121-35-443'


    if id_check(license_plate) != str(1):
        return (f"your truck id : {license_plate} is not exist! please try again.", 409)

    else:
        if id_check(new_license_plate) != str(0):
            return (f"your new truck id : {new_license_plate} is already exist! please try again.", 409)
        else:
            update_data = my_sql.updateData(f'UPDATE Trucks SET id = "{new_license_plate}" WHERE id ="{license_plate}";')
            return(f"Enjoy! your old license plate : {license_plate} changed to {new_license_plate}!", 200)



if __name__ == '__main__':
    PUT_truck()    
