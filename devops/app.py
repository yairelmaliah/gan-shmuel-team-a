from flask import Flask , request
import os
from config import *
from run_tests import run_test
from mailing import send_mail

app = Flask(__name__)

def build_app(data):
    # Extract data from github request
    branch_name = data['ref'].split('/')[-1]
    pusher_github_name = data["pusher"]["name"]
    
    if branch_name not in BRANCHES_ALLOWED:
        return "Branch is not allowed, abort...", 405

    # Generate emails according to branch and pusher
    try:
        leader_email = CONTACT_EMAILS[f'{branch_name}_team']["team_members"][CONTACT_EMAILS[f'{branch_name}_team']["team_leader"]]
        pusher_email = CONTACT_EMAILS[f'{branch_name}_team']["team_members"][pusher_github_name]
    except:
        print(f"Pusher email not exist in our system please add him --> {pusher_github_name}")

    # Remove previous test clone, and clone new changes
    os.system(f'rm -rf {TEST_TMP_PATH}')
    os.system(f'git clone -b {branch_name} --single-branch {REPO} {TEST_TMP_PATH}')

    # Run tests
    test_results = run_test(branch_name)
    print(test_results, flush=True)

    # Test success
    if not b'ERROR' in test_results:
        # Logs
        print("All tests passed successfully !!", flush=True)
        print("Removing test containers ...", flush=True)

        # Remove temporary test containers
        os.system(f'docker rm -f {TEST_CONTAINERS_NAMES[branch_name]}')

        # Send success results to pusher's/leader's email address
        subject = HEADING_SUCCESS
        if leader_email == pusher_email:
            send_mail([leader_email],subject,test_results)
        else:    
            send_mail([leader_email,pusher_email],subject,test_results)

        # Deploy new version
        print("Deploy new app version...", flush=True)
        os.system(f'docker-compose -f {TEST_TMP_PATH}/{branch_name}/docker-compose.yaml -f {TEST_TMP_PATH}/{branch_name}/docker-compose.prod.yaml up --build -d')
    
    # Test failure
    else:
        # Logs
        print("Tests failed, removing tests containers and aborting ...", flush=True)

        # Remove temporary test containers
        os.system(f'docker rm -f {TEST_CONTAINERS_NAMES[branch_name]}')

        # Send failure results to pusher's/leader's email address
        subject = HEADING_FAILURE
        if leader_email == pusher_email:
            send_mail([leader_email],subject,test_results)
        else:
            send_mail([leader_email,pusher_email],subject,test_results)

        # Abort
        exit(0)
    
    exit(1)


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
    return build_app(data)
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8082, debug=True)
