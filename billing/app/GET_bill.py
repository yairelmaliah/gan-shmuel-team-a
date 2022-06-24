
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

 ##################################### check data ####################################    
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

        if from_date > to_date:
            return("from date is larger than to date. please try again.", 409)

        if len(from_date) != 14 or from_date.isnumeric() == False:
            return (f"from_date is not valid, please try again.", 409)

        elif len(to_date) != 14 or to_date.isnumeric() == False:
            return ("to_date is not valid, please try again.", 409)

    except :

        from_date = currentDT.strftime("%Y%m01000000")
        to_date = currentDT.strftime("%Y%m%d%H%M%S")



    is_exists = my_sql.getData(f"SELECT EXISTS(SELECT id FROM Trucks WHERE provider_id='{provider_id}');")
    dump = json.dumps(is_exists)
    value = str(dump[-3])
    
    if value == str(0):
        return (f"Provider id : {provider_id} does not have a license plate, please try again.", 404)


##################################  Starting bill ##############################


    licenses = list(my_sql.getData(f'SELECT id FROM Trucks WHERE provider_id={provider_id};'))
    truck_count = len(licenses)
    session_count = 0
   #print(f"license : {licenses}")
    total=0
    


    weighted_containers = requests.get(f"http://3.66.68.27:8081/weight?from={from_date}&to={to_date}&filter=out").json()
    weighted_containers = json.dumps(weighted_containers)
    weighted_containers = json.loads(weighted_containers)

    
    sessions = []

  #  print(weighted_containers['data'][0])
    #Get all sessions that are specific to this provider
    for truck in weighted_containers['data']:
        for truck_id in licenses:
            if truck['truck'] == str(truck_id['id']):
                sessions.append(truck)
                session_count += 1



    providers_products=[]

    for truck in sessions:
        flag=0
        for product in providers_products:
            if truck['produce'] == product['product']:
            #    product['count'] += 1
                product['amount'] += truck['neto']
                product['pay'] += product['rate']*truck['neto']
                total += product['rate']*truck['neto']
                flag=1


        exist_check = my_sql.getData(f"""SELECT EXISTS(SELECT product_id FROM Rates WHERE product_id='{truck['produce']}');""")
        dump = json.dumps(exist_check)
        value = str(dump[-3])
        if value == str(0):  
            return (f"Produce: {truck['produce']} does not apear in our rates, please upload new rates and try again.", 404)


        
        if flag == 0:
            rate_data = my_sql.getData(f"""SELECT rate FROM Rates WHERE product_id='{truck['produce']}' AND scope={provider_id};""")


             
            if len(rate_data) == 0:
                rate_data = my_sql.getData(f"""SELECT rate FROM Rates WHERE product_id='{truck['produce']}' AND scope='ALL';""")

            rate_price = (rate_data[0]['rate'])


            providers_products.append({
            "product": truck['produce'],
            "count" : 1,
            "amount" : truck['neto'],
            "rate": rate_price,
            "pay" : truck['neto']*rate_price
            })
            total += rate_price*truck['neto']


    recipet = {
        "id": provider_id,
        "name": "test",
        "from": from_date,
        "to": to_date,
        "truckCount": truck_count,
        "sessionCount": session_count,
        "products": providers_products,
        "total": total
    }
    
    return recipet
    
if __name__ == '__main__':
    GET_bill(id)    









    # truck_count = 0
    # items = []

    # for one in licenses:
    #     truck_count += 1
    #     plate = one['id']
        
    #     license_list += {one['id']}
    #     items.append(requests.get(f"http://3.66.68.27:8081/item/{plate}?from{from_date}to{to_date}").json())


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

  