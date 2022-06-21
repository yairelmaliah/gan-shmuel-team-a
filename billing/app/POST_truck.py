from http.client import OK
import mimetypes
from sqlite3 import IntegrityError
from urllib import response
import requests
from flask import Flask, render_template, request
import json
from db_utils import db_utils


my_sql = db_utils()



def POST_truck():

    provider_id = '10003'
    truck_id = '134-35-443'

    id = my_sql.getData(f'SELECT EXISTS(SELECT * FROM Provider WHERE id={provider_id});')
    x = json.dumps(id)
    value = str(x[-3])

    if value == str(0):
        return (f"Provider id : {provider_id} not found, please try again.", 409)
    
    else:

       id_check = my_sql.getData(f'SELECT EXISTS(SELECT * FROM Trucks WHERE id="{truck_id}");')
       y = json.dumps(id_check)
       value_id = str(y[-3])

       if value_id == str(1):
            return (f"truck id : {truck_id} is already exist! please try again.", 409)

       else:
            my_sql.setData(f"INSERT INTO Trucks(id, provider_id) VALUES('{str(truck_id)}', '{str(provider_id)}')")
            return (f"inserted : truck_id {truck_id} to provider id : {provider_id}", 200)
        


if __name__ == '__main__':
    POST_truck()    
