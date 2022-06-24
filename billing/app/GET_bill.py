
import requests
from flask import request
import json
from db_utils import db_utils
from datetime import datetime
#import werkzeug


my_sql = db_utils()

   
def GET_bill(id):

 ##################################### check data ####################################    
    currentDT = datetime.now()
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


##################################  CHECKING DATA ##############################


    licenses = list(my_sql.getData(f'SELECT id FROM Trucks WHERE provider_id={provider_id};'))

    
    data_name = (my_sql.getData(f"""SELECT name FROM Provider WHERE id='{provider_id}';"""))
    t = json.dumps(data_name)
    d = json.loads(t)
    provider_name = d[0]['name']

    try:
        weighted_containers = requests.get(f"http://3.66.68.27:8081/weight?from={from_date}&to={to_date}&filter=out").json()
        weighted_containers = json.dumps(weighted_containers)
        weighted_containers = json.loads(weighted_containers)

    except requests.exceptions.JSONDecodeError:
        return (f"Provider id : {provider_id} does not have bill for those dates.")

    total=0
    truck_count = len(licenses)
    session_count = 0


    sessions = []
    for truck in weighted_containers['data']:
        for truck_id in licenses:
            if truck['truck'] == str(truck_id['id']):
                sessions.append(truck)
                session_count += 1

    
    providers_products=[]

    for truck in sessions:
        flag=0
        truck_product = truck['produce']
        truck_neto = truck['neto']

###################  checking products bill ##############
    

        for product in providers_products:
            if truck_product == product['product']:
                product['count'] += 1
                product['amount'] += truck_neto
                product['pay'] += product['rate']*truck_neto
                total += product['rate']*truck_neto
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
            "product": truck_product,
            "count" : 1,
            "amount" : truck_neto,
            "rate": rate_price,
            "pay" : truck_neto*rate_price
            })
            total += rate_price*truck_neto



    recipet = {
        "id": provider_id,
        "name": provider_name,
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
