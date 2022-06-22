from flask import Flask, render_template, request
from db import Mysql
from handlers.batch_weight_handler import batch_weight_handler
from handlers.post_weight_handler import post_weight_handler
from handlers.get_weight_handler import get_weight_handler
from handlers.get_session_handler import get_session_handler
from handlers.get_item_handler import get_item_handler
from handlers.get_unknown_handler import get_unknown_handler

app = Flask(__name__)

# ======================================
# Main Routes
# ======================================
@app.route("/")
def home():
  return "Welcome to weight system", 200

@app.route("/health")
def health():
  return "ok" , 200

@app.route("/weight", methods=["POST","GET"])
def post_weight():
  if request.method == 'POST':
    return post_weight_handler(request.args)
  if request.method == 'GET':
    return get_weight_handler(request.args)

@app.route("/batch-weight/<file>", methods=["POST"])
def batch_weight(file):
  return batch_weight_handler(file)

@app.route("/session/<id>")
def get_session(id):
  return get_session_handler(id)

@app.route("/item/<id>")
def get_item(id):
  return get_item_handler(request.args,id)

@app.route("/unknown")
def get_unknown():
  return get_unknown_handler()


# ======================================
# Errors handling
# ======================================
@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', error= e), 404

@app.errorhandler(400)
def bad_request(e):
    return render_template('bad-request.html', error= e), 400

@app.errorhandler(405)
def not_allowed(e):
    return "You are trying to access a route with an unsuported method, check again your method!!", 405

# ======================================
# Start
# ======================================
if __name__ == '__main__':
  app.run(host="0.0.0.0",port=8081, debug=True)