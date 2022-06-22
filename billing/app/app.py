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



app = Flask(__name__)

@app.route('/')
@app.route('/home')
# @app.route('/index')
def index():
    return render_template('index.html')


@app.route("/health", methods=['GET','POST'])
def health():
    return health_check()

@app.route("/health")
def health_web():
    return render_template(index.html)


@app.route("/api/health")
def api_web_health():
    return render_template(index.html)






############################################
########### Providers ####################



#### POST PROVIDER

@app.route("/api/provider", methods=['POST'])
def post_api_provider():
    return POST_provider()


@app.route("/provider", methods=['POST'])
def post_provider():
    return POST_provider()


### GET PROVIDER ###

@app.route("/api/provider", methods=['GET'])
def post_provider_render():
    return render_template('provider.html')

@app.route("/provider")
def provider():
    return render_template('provider.html')
    # return POST_provider()


########### PUT PROVIDER ID ######


@app.route("/api/provider/<id>/", methods=['PUT'])
def put_api_provider_id(id):
        return PUT_provider(id)


@app.route("/provider/<id>/", methods=['PUT'])
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


############################################
################### Trucks #################


### POST TRUCK ####
@app.route("/api/truck", methods=['POST'])
def post_api_truck():
    return POST_truck()


@app.route("/truck", methods=['POST'])
def post_truck():
    return POST_truck()

### GET TRUCK ###

@app.route("/api/truck", methods=['GET'])
def post_api_truck_render():
    return render_template('truck.html')


@app.route("/truck", methods=['GET'])
def post_truck_render():
    return render_template('truck.html')


@app.route("/truck/")
def truck():
    return render_template('truck.html')


### PUT TRACK ID ###

@app.route('/api/truck/<id>/', methods=['PUT'])
def put_api_truck(id):
        return PUT_truck(id)


@app.route('/truck/<id>/', methods=['PUT'])
def put_truck(id):
        return PUT_truck(id)

### GET TRUCK ID ####

@app.route("/api/truck/<id>/", methods=['GET'])
def get_api_truck_id(id):
    return GET_truck(id)

@app.route("/truck/<id>/", methods=['GET'])
def get_func_truck_id(id):
    return GET_truck(id)

@app.route("/api/truck/<id>/")
def get_api_func_truck_id():
    return render_template('index.html')

@app.route("/truck/<id>/")
def get_truck_id():
    return render_template('index.html')


#######################################################
################### RATES #############################


### POST RATES ###


@app.route("/api/rates/<file>", methods=['POST'])
def api_rates(file):
   return POST_rates(file)


@app.route("/rates/<file>", methods=['POST'])
def rates(file):
   return POST_rates(file)

@app.route("/api/rates/<file>")
def rates_api_web():
    return render_template('index.html')

@app.route("/rates/<file>")
def rates_web():
    return render_template('index.html')


#### GET RATES ###

@app.route("/api/rates", methods=['GET'])
def get_api_rates():
   return GET_rates()

@app.route("/rates", methods=['GET'])
def get_rates():
   return GET_rates()


@app.route("/api/rates")
def get_api_rates_web():
    return render_template('index.html')

@app.route("/rates")
def get_rates_web():
    return render_template('index.html')


####################################################
################# BILL #############################


@app.route("/api/bill/<id>", methods=['GET'])
def get_api_bill(id):
   return GET_bill(id)

@app.route("/bill/<id>", methods=['GET'])
def get_bill(id):
   return GET_bill(id)

@app.route("/api/bill/<id>")
def get_render_bill():
    return render_template('index.html')


@app.route("/bill/<id>")
def get_render_bill_web():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
