from flask import Flask, render_template
from script import *
app = Flask(__name__)

@app.route("/monitor")
def monitor():
    portstatus()
    return render_template('index.html')

@app.route("/monitor/openports.txt")
def ports():
    with app.open_resource('open_ports.txt') as f:
        contents = f.read()
    return contents

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
