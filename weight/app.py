from flask import Flask, render_template, request
from db import Mysql
from batch_weight_handler import batch_weight_handler
from post_weight_handler import post_weight_handler


app = Flask(__name__)

@app.route("/")
def home():
  return "hello world", 200

@app.route("/health")
def health():
  return render_template("index.html") , 200



@app.route("/post_weight")
def post_weight():
  print(request.args, flush=True)
  return "sadasdsa"
  return post_weight_handler()

@app.route("/batch_weight/<file>", methods=["POST", "GET"])
def batch_weight(file):
  return batch_weight_handler(file)


app.run(host="0.0.0.0",port=8081, debug=True)