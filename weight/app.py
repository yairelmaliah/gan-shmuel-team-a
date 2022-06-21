from flask import Flask, render_template
from db import Mysql
from batch_weight import batch_weight
app = Flask(__name__)

@app.route("/")
def home():
  return "hello world", 200

@app.route("/health")
def health():
  return render_template("index.html") , 200

@app.route("/batch_weight/<file>", methods=["POST", "GET"])
def post_batch_weight(file):
  return batch_weight(file)


app.run(host="0.0.0.0",port=8081, debug=True)