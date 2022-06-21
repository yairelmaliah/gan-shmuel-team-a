from flask import Flask, render_template, request
from GET_health import GET_health
from POST_provider import POST_provider
from PUT_provider import PUT_provider
from POST_truck import POST_truck
from PUT_truck import PUT_truck
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
    return GET_health()


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


@app.route("/api/provider/<id>", methods=['PUT'])
def put_provider_id(id):
        return PUT_provider(id)

@app.route("/api/provider/<id>/", methods=['GET'])
def put_provider_render():
    return render_template('provider_id.html')

@app.route("/provider/<int:id>")
def provider_id(id):
    if id < 10001:
       return f'You are not allowed - Id does not exist'
    else:
        return render_template('provider_id.html')
    
@app.route('/truck', methods=['POST'])
def post_truck():
    return POST_truck()

@app.route('/truck/1000', methods=['PUT'])
def put_truck():
    return PUT_truck()


if __name__ == '__main__':
    # billingdb = mysql.connector.connect(
    #     host="billingdb",
    #     user="root",
    #     password="1234!",
    #     database='billdb',
    # )
    app.run(debug=True, host='0.0.0.0', port=5000)
