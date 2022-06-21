from flask import Flask, render_template, request
from GET_health import GET_health
from POST_provider import POST_provider
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

@app.route('/provider')
def provider():
    return render_template('provider.html')


@app.route("/provider/<id>", methods=['PUT'])
def put_provider_id():
    pass

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
