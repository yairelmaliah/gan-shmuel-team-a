from flask import Flask, render_template, request
from db import Mysql
from handlers.batch_weight_handler import batch_weight_handler
from handlers.post_weight_handler import post_weight_handler
from handlers.get_weight_handler import get_weight_handler
from handlers.get_session_handler import get_session_handler
from handlers.get_item_handler import get_item_handler
from handlers.get_unknown_handler import get_unknown_handler

app = Flask(__name__)

@app.route("/")
def home():
  return "Welcome to weight system", 200

@app.route("/health")
def health():
  return "ok" , 200

@app.route("/post_weight", methods=["POST"])
def post_weight():
  return post_weight_handler(request.args)

@app.route("/batch_weight/<file>", methods=["POST"])
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

@app.route("/get_unknown")
def get_unknown():
  return get_unknown_handler()

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('error.html', error= e), 404

@app.errorhandler(400)
def bad_request(e):
    # note that we set the 404 status explicitly
    return render_template('bad-request.html', error= e), 400

@app.errorhandler(405)
def not_allowed(e):
    # note that we set the 404 status explicitly
    return "You are trying to access a route with an unsuported method, check again your method!!", 404

if __name__ == '__main__':
  app.run(host="0.0.0.0",port=8081, debug=True)