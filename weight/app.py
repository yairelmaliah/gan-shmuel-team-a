from flask import Flask, render_template, request
from db import Mysql
from batch_weight_handler import batch_weight_handler
from post_weight_handler import post_weight_handler
from get_weight_handler import get_weight_handler
from get_session_handler import get_session_handler
from get_item_handler import get_item_handler

app = Flask(__name__)

@app.route("/")
def home():
  return "hello world", 200

@app.route("/health")
def health():
  return render_template("index.html") , 200

@app.route("/post_weight")
def post_weight():
  return post_weight_handler(request.args)

@app.route("/batch_weight/<file>", methods=["POST", "GET"])
def batch_weight(file):
  return batch_weight_handler(file)

@app.route("/get_weight")
def get_weight():
  return get_weight_handler(request.args)

@app.route("/get_session/<id>")
def get_session(id):
  return get_session_handler(id)

@app.route("/get_item/<id>")
def get_item(id):
  return get_item_handler(request.args,id)

app.run(host="0.0.0.0",port=8081, debug=True)