import os

DYNAMIC_PATH = str(os.environ.get('DYNAMIC_PATH'))
REPO = 'https://github.com/Julianius/GanShmuel.git'
SUCCESS_CODE = 0
FAILURE_CODE = 1

PATH_APP = '/gan-shmuel-team-a/app/'
WEIGHT='Weight'
BILLING='Billing'
DEVOPS='Devops'

DOCKER_COMPOSE_PATHS = { 
  'weight': '/weight/docker-compose.yaml',
  'billing': '/billing/docker-compose.yaml'
}


MESSAGE_SUCCESS = 'All tests passed successfully!'
MESSAGE_FAILURE = 'Some tests have failed. Please check!'

MESSAGE_SUCCESS_DEPLOY = 'System has been deployed successfully! System is running and operational.'
MESSAGE_FAILURE_DEPLOY = 'System was not deployed successfully. Please check!'

CONTACT_EMAILS = {
    "weight_team": {
        "yair": "yairelmaliah319732@gmail.com"
    },

    "billing_team": {
        "rotem": "kalmanrotem@gmail.com"
    },

    "devops_team": {
        "ori": "orimeyuhas@gmail.com"
    }
}    