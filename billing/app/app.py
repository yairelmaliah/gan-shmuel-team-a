from flask import Flask, render_template, request
from GET_health import GET_health
from POST_provider import POST_provider
from PUT_provider import PUT_provider
from POST_truck import POST_truck
from PUT_truck import PUT_truck
from GET_truck import GET_truck
from POST_rates import POST_rates
from GET_rates import GET_rates
from GET_bill import GET_bill
from health_check import health_check
import requests



app = Flask(__name__)

@app.route('/')
@app.route('/home')
# @app.route('/index')
def index():
    return render_template('index.html')

@app.route("/health", methods=['GET','POST'])
def health():
    return "OK", 200

# @app.route("/health")
# def health_web():
#     return render_template(index.html)


# @app.route("/api/health")
# def api_web_health():
#     return render_template(index.html)



############################################
########### Providers ####################


@app.route("/api/provider", methods=['POST'])
def post_api_provider():
    return POST_provider()

@app.route('/provider/<id>/', methods=['PUT'])
def put_provider(id):
    return PUT_provider(id)

@app.route("/api/provider", methods=['GET'])
def post_provider_render():
    return render_template('provider.html')

@app.route("/provider")
def provider():
    return render_template('provider.html')

@app.route("/provider/<int:id>/")
def provider_id(id):
    if id < 10001:
       return f'You are not allowed'
    else:
        return render_template('provider_id.html')


############################################
################### Trucks #################

@app.route("/truck")
def truck():
    return render_template('truck.html')

@app.route("/truck/update")
def update_truck_id():
    return render_template('truck_id.html')

@app.route("/truck/fetch")
def fetch_truck_id():
    return render_template('truck_fetch.html')

@app.route("/api/truck", methods=['POST'])
def post_api_truck():
    return POST_truck()

@app.route('/truck/<truck_id>', methods=['PUT'])
def put_api_truck(truck_id):
        return PUT_truck(truck_id)

@app.route('/truck/<truck_id>', methods=['GET'])
def fetch_truck(truck_id):
        return GET_truck(truck_id)


#######################################################
################### RATES #############################


@app.route("/api/rates/<file>", methods=['POST'])
def api_rates(file):
   return POST_rates(file)

@app.route("/api/rates", methods=['GET'])
def fetch_rates():
   return GET_rates()

@app.route("/rates")
def get_rates_web():
    return render_template('rates.html')

@app.route("/rates/fetch")
def get_rates_message():
    return render_template('rates_fetch.html')

# @app.route("/rates/<file>", methods=['POST'])
# def rates(file):
#    return POST_rates(file)

# @app.route("/api/rates/<file>")
# def rates_api_web():
#     return render_template('index.html')

# @app.route("/rates/<file>")
# def rates_web():
#     return render_template('index.html')


#### GET RATES ###

# @app.route("/api/rates", methods=['GET'])
# def get_api_rates():
#    return GET_rates()

# @app.route("/rates", methods=['GET'])
# def get_rates():
#    return GET_rates()

# @app.route("/api/rates")
# def get_api_rates_web():
#     return render_template('index.html')

####################################################
################# BILL #############################

@app.route("/bill/<id>", methods=['GET'])
def get_bill(id):
   return GET_bill(id)


@app.route("/bill")
def get_render_bill_web():
    return render_template('bill.html')



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
