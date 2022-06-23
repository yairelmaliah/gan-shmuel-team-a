from flask import Flask, render_template, request
from GET_health import GET_health
from POST_provider import POST_provider
from PUT_provider import PUT_provider
from POST_truck import POST_truck
from PUT_truck import PUT_truck
from GET_truck import GET_truck
from POST_rates import POST_rates
from GET_rates import GET_rates

import mysql.connector
import time

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="billing",
#   password="billing"
# )

# ###print(mydb)


app = Flask(__name__)

@app.route('/')
# @app.route('/index')
def index():
    return render_template('index.html')


@app.route("/health", methods=['GET','POST'])
def health():
    return "ok", 200
    # return GET_health()

########### Providers #############

@app.route("/api/provider", methods=['POST'])
def post_provider():
    return POST_provider()

@app.route("/api/provider", methods=['GET'])
def post_provider_render():
    return render_template('provider.html')

@app.route("/provider")
def provider():
    return render_template('provider.html')
    # return POST_provider()


@app.route("/api/provider/<id>/", methods=['PUT'])
def put_provider_id(id):
        return PUT_provider(id)

@app.route("/api/provider/<id>/", methods=['GET'])
def put_provider_render():
    return render_template('provider_id.html')
    

@app.route("/provider/<int:id>")
def provider_id(id):
    if id < 10001:
       return f'You are not allowed'
    else:
        return render_template('provider_id.html')



######## Trucks #############

@app.route("/api/truck", methods=['POST'])
def post_truck():
    return POST_truck()


@app.route("/api/truck", methods=['GET'])
def post_truck_render():
    return render_template('truck.html')

@app.route("/truck/")
def truck():
    return render_template('truck.html')


@app.route('/truck/<id>/', methods=['PUT'])
def put_truck(id):
        return PUT_truck(id)


@app.route("/api/truck/<id>/", methods=['GET'])
def get_api_truck_id(id):
    return GET_truck(id)


@app.route("/api/truck/<id>/", methods=['GET'])
def get_truck_id_render(id):
    return GET_truck(id)

@app.route("/truck/<id>/")
def get_truck_id():
    return render_template('index.html')



#### RATES ####

@app.route("/api/rates/<file>", methods=['POST'])
def rates(file):
   return POST_rates(file)

@app.route("/api/rates/<file>")
def rates_web():
    return render_template('index.html')



@app.route("/api/rates", methods=['GET'])
def get_rates():
   return GET_rates()


@app.route("/api/rates")
def get_rates_web():
    return render_template('index.html')


##### API FOR WEIGHT ####


@app.route("/api/information", methods=['GET'])
def get_information():
    return get_information()


if __name__ == '__main__':
    # billingdb = mysql.connector.connect(
    #     host="billingdb",
    #     user="root",
    #     password="1234!",
    #     database='billdb',
    # )
    app.run(debug=True, host='0.0.0.0', port=5000)
