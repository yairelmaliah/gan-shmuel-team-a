REPO = 'https://github.com/yairelmaliah/gan-shmuel-team-a.git'

BRANCHES_ALLOWED = ['weight', 'billing']

SENDER_EMAIL = 'develeapblueteum@gmail.com'
PASSWORD = 'cehjgdpczgllgyzs'
SERVER_NAME = 'smtp.gmail.com'
SERVER_PORT = 587

CONTACT_EMAILS = {
    "weight_team": {
        "team_leader": "yairelmaliah",
        "team_members": {
            "yairelmaliah": "yairelmaliah319732@gmail.com",
            "davidab265": "",
            "Gologolo97": "lejbgolovaty@yahoo.com"
        }
    },

    "billing_team": {
        # "team_leader": "RotemK1",
        "team_leader": "yairelmaliah",
        "team_members": {
            "yairelmaliah": "yairelmaliah319732@gmail.com",
            "RotemK1": "kalmanrotem@gmail.com",
            "asi111": "",
            "oshriza": ""
        }
    },

    "devops_team": {
        "team_leader": "OriMeyuhas",
        "team_members": {
            "OriMeyuhas": "orimeyuhas@gmail.com",
            "yairelmaliah": "yairelmaliah319732@gmail.com",
            "adelwa": "adelw@post.bgu.ac.il",
            "evra3": "abrahem.mhajnee@gmail.com",
            "RotemHaim6": ""
        }
    }
}

HEADING_SUCCESS = 'All tests passed successfully!'
HEADING_FAILURE = 'Some tests have failed. Please check!'

TEST_TMP_PATH = "/tmp/gan-shmuel-app"

TEST_CONTAINERS_NAMES = {
    "weight": "weight_app_test sql_test",
    "billing": "billing_db_test billing_app_test",
}