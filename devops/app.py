from flask import Flask , request
import os
import json

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def home():
    return "OK", 200


@app.route('/health', methods = ['GET'])
def health():
    return "OK", 200

@app.route('/webhook', methods = ['POST'])
def webhook():
    data = request.get_json()
    f = open('dump.txt', 'w')
    text = str(data)
    f.write(text)
    f.close()
    #master_branch = (data['repository']['master_branch'])
    #branch=(data['ref']).split("/")[-1]
    os.system('cd ~/Gan-shmuel-project-A')
    os.system('git pull origin devops')
    os.system('cd devops')
    os.system('docker build -t prod/gan:v1')

    return "OK", 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
