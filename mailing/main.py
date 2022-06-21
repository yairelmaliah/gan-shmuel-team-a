from flask import request
import json
import os

from config import *
from email_app import *

def print_hi():
    with open('aa.json') as json_file:
        data = json.load(json_file)


###########################################
    #email function

    pusher=data['pusher']['name']
    # print(pusher)

    subject = ""
    team_lead_email = ""
    pusher_email = ""
    for team in CONTACT_EMAILS.items():
        if pusher in team[1]:
            subject=team[0]
            if team[0] == "weight_team":
                team_lead_email = CONTACT_EMAILS["weight_team"]['team_leader']
                pusher_email = CONTACT_EMAILS["weight_team"][pusher]
            elif team[0] == "billing_team":
                team_lead_email = CONTACT_EMAILS["billing_team"]['team_leader']
                pusher_email = CONTACT_EMAILS["billing_team"][pusher]
            else:
                team_lead_email = CONTACT_EMAILS["devops_team"]['team_leader']
                pusher_email = CONTACT_EMAILS["devops_team"][pusher]
            break
    branchName = (data['ref']).split("/")[-1]
    if branchName in BRANCHES_ALLOWED:
        os.system('rm -rf ' + PATH_APP + 'temp')
        print('git clone -b ' + branchName + ' ' + REPO + ' ' + PATH_APP + 'temp')
        os.system('git clone -b ' + branchName + ' ' + REPO + ' ' + PATH_APP + 'temp')
        test_result = "test success"            #DEFAULT
        #test_result = run_test function boolean value()
        test_result=True
        status="test failure"
        if test_result:
            status="test success"
        if test_result == False:
            send_email(subject, status, team_lead_email, pusher_email)
        else:   #TRUE
            if branchName != "master":         #Development
                send_email(subject, status, team_lead_email, pusher_email)
            else:                              #Deploy
                os.system('rm -rf ' + PATH_APP + branchName)
                os.system('mkdir -p ' + PATH_APP + branchName)
                os.system('mv ' + PATH_APP + 'temp/* ' + PATH_APP + 'temp/.* ' + PATH_APP + branchName + '/ 2>/dev/null')
                os.system('rm -rf ' + PATH_APP + 'temp')
                os.system('cd ' + PATH_APP + branchName)
                send_email(subject, status, team_lead_email, pusher_email)



    else:
        print("nana")
        #send a message


if __name__ == '__main__':
    print_hi()