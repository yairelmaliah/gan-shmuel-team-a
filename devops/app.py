from cgi import test
from flask import Flask , request
import os
import shutil
from config import *
from run_tests import run_test

app = Flask(__name__)

def build_app(data):
    branch_name = data['ref'].split('/')[-1]
    pusher_github_name = data["pusher"]["name"]
    os.system('rm -rf /tmp/gan-shmuel-app')
    # os.system(f'git clone -b {branch_name} --single-branch {REPO} /tmp/gan-shmuel-app')
    os.system(f'git clone -b {branch_name} --single-branch {REPO} /tmp/gan-shmuel-app')
    # Run tests:
    test_results = run_test(branch_name)

    print("=====================================", flush=True)
    print(test_results, flush=True)
    print("=====================================" ,flush=True)
    return "ok"
    os.system(f'docker-compose -f /home/develeap/bootcamp/Gan-Shmuel-Project/gan-shmuel-team-a/{branch_name}/docker-compose.yaml up --build -d')

    if os.path.isdir(PATH_TEST):
        shutil.rmtree(PATH_TEST)
    os.mkdir(PATH_TEST)
    os.chdir(PATH_TEST)
    os.system(f'git clone -b {branch_name} --single-branch {REPO}')
    os.system(f'docker-compose -f /home/develeap/bootcamp/Gan-Shmuel-Project/gan-shmuel-team-a/{branch_name}/docker-compose.yaml up --build -d')


@app.route('/', methods = ['GET'])
def home():
    return "OK", 200

@app.route('/health', methods = ['GET'])
def health():
    return "OK changed", 200

@app.route('/webhook', methods = ['POST'])
def webhook():
    data = request.get_json()
    print(data,flush= True)
    build_app(data)
    
    return "OK", 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8082, debug=True)

