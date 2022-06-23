from flask import Flask, render_template
from script import *
import sys
app = Flask(__name__)


dev = False

if "dev" in sys.argv:
  dev = True

@app.route("/monitor")
def monitor():
    portstatus(dev)
    return render_template('index.html')

@app.route("/monitor/openports.txt")
def ports():
    with app.open_resource('open_ports.txt') as f:
        contents = f.read()
    return contents

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8085, debug=True)
