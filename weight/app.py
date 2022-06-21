from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def home():
  return "hello world", 200

@app.route("/health")
def health():
  return render_template("index.html") , 200

app.run(host="0.0.0.0",port=3000, debug=True)