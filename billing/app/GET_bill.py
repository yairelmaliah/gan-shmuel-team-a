
import requests
from flask import request
import json
from db_utils import db_utils
import datetime
#import werkzeug
from requests import Session
from requests.adapters import HTTPAdapter
from requests.exceptions import ConnectionError
from enum import Enum
class LOG_TYPE(Enum):
    INFO=0
    ERROR=1
    WARNING=2

type_desc = ["[INFO]","[ERROR]","[WARNING]"]
def LOG(str,TYPE):
    datObj = datetime.now()
    with open("log","a+") as f:
        f.write(f'[{datObj}] {type_desc[TYPE.value]} {str}\n')

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

    except :

        from_date = currentDT.strftime("%Y%m01000000")
        to_date = currentDT.strftime("%Y%m%d%H%M%S")


    is_exists = my_sql.getData(f"SELECT EXISTS(SELECT id FROM Trucks WHERE provider_id='{provider_id}');")
    dump = json.dumps(is_exists)
    value = str(dump[-3])
    
    if value == str(0):
        return (f"Provider id : {provider_id} does not have a license plate, please try again.", 404)


    licenses = list(my_sql.getData(f'SELECT id FROM Trucks WHERE provider_id={provider_id};'))

    
#     truck_count = 0
#     items = []
 
#     for one in licenses:
#         truck_count += 1
#         plate = one['id']
        
#       # license_list += {one['id']}
#         items.append(requests.get(f"http://localhost:5000/item/{plate}?from{from_date}to{to_date}").json())


#     #return str(items)

    
#    # http://3.66.68.27:8081/weight?from=20220122190746to=20220722190746&filter=out
    
#     weighted_containers = requests.get(f"http://3.66.68.27:8081/weight?from=20210122190746to=20230722190746&filter=out")

#     providers_sessions = []

#     #Get all sessions that are specific to this provider
#     for truck in weighted_containers:
#         for truck_id in licenses:
#             #LOG(truck['id'],LOG_TYPE.INFO)
#             if truck['id'] == truck_id:
#                 providers_sessions.append(truck)

#     #return int(1)
#     #requests.get(f"http://localhost:5000/item/{license_plate}?from{from_date}to{to_date}").json()

    # d = requests.get(f"http://localhost:5000/weight/{license_plate}?from{from_date}to{to_date}").json()

  
    name = ""

    truckCount=0
    total=0
    result_arr = licenses

    #We expect to get a json array for all trucks that went out
    #headers = {"Accept": "application/json"}
    weighted_containers = requests.get(f"http://3.66.68.27:8081/weight?from={from_date}to={to_date}&filter=out").json()
    
    return weighted_containers
    
    print(a[0], flush=True)
    return "asdsadsad"
    #weighted_containers = requests.get("http://3.66.68.27:8081/weight?from=20210122190746to=20230722190746&filter=out")

    #return weighted_containers.text
    #weighted_containers = "[(10002, 'out', 'C-3123', 5000, None, 'Blood'), (10005, 'out', 'C-7123', 5000, None, 'Mandarin'), (10006, 'out', 'C-8123', 5000, None, 'Navel'), (10008, 'out', 'C-3123', 5000, None, 'Tangerine')]"
    text = BeautifulSoup(weighted_containers.text, features="html.parser").prettify()
    print(json.loads(text), flush=True)

    print(weighted_containers.json(), flush=True)
    
    return "dfsfsdfd"
    
    

    #trey = ''.join(test)
    print(weighted_containers.text[1], flush=True)
    return "x"
    #TODO Number of sessions for each product
    #TODO Get total weight of each product

    providers_sessions = []

    #Get all sessions that are specific to this provider
    for truck in weighted_containers:
        for truck_id in result_arr:
            LOG(truck['id'],LOG_TYPE.INFO)
            if truck['id'] == truck_id:
                providers_sessions.append(truck)

    providers_products=[]

    for truck in providers_sessions:
        flag=0
        for product in providers_products:
            if truck['produce'] == product['name']:
                product['count'] += 1
                product['amount'] += truck['neto']
                product['pay'] += product['rate']*truck['neto']
                total += product['rate']*truck['neto']
                flag=1


     #   if flag == 0:#No Products were found in the list we add it
            #Fetch the rates for this specific provider
           # sql_query = f"SELECT rate FROM Rates WHERE product_id={truck['produce']} AND scope={id};"
          #  rates_arr = my_sql.getData(sql_query)
           
        #    if len(rates_arr) == 0:#We didn't find speific rate for this provider we have to look for ALL scope
           #     sql_query = f"SELECT rate FROM Rates WHERE product_id={truck['produce']} AND scope='ALL'"
                
           #     rates_arr = my_sql.getData(sql_query)
            #TODO for now we assume product is found in rates but that's not always the case so we have to add another check

            # providers_products.append({
            #     "name": truck['produce'],
            #     "count" : 1,
            #     "amount" : truck['neto'],
            #     "rate": int(rates_arr[0][0]),
            #     "pay" : truck['neto']*int(rates_arr[0][0])
            # })
            # total += int(rates_arr[0][0])*truck['neto']
    
if __name__ == '__main__':
    GET_bill(id)    
