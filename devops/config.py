import os

DYNAMIC_PATH = str(os.environ.get('DYNAMIC_PATH'))
REPO = 'https://github.com/yairelmaliah/gan-shmuel-team-a.git'
SUCCESS_CODE = 0
FAILURE_CODE = 1

PATH_APP = '/gan-shmuel-team-a/app'
PATH_TEST = '/home/develeap/bootcamp/Gan-Shmuel-Project/test'
WEIGHT='Weight'
BILLING='Billing'
DEVOPS='Devops'
BRANCHES_ALLOWED = [ 'devops', 'weight', 'billing' ]

DOCKER_COMPOSE_PATHS = { 
  'weight': '/weight/docker-compose.yaml',
  'billing': '/billing/docker-compose.yaml'
}
APPS_DB_PATHS = {
  'weight': DYNAMIC_PATH + 'app/weight-staging/weight',
  'billing': DYNAMIC_PATH + 'app/billing-staging/billing'
}

APPS_PATHS = {
  'weight': DYNAMIC_PATH + 'app/weight-staging/weight',
  'billing': DYNAMIC_PATH + 'app/billing-staging/billing'
}

TEST_APPS_DB_PATHS = {
  'weight': DYNAMIC_PATH + 'test/weight-staging/weight',
  'billing': DYNAMIC_PATH + 'test/billing-staging/billing'
}

TEST_APPS_PATHS = {
  'weight': DYNAMIC_PATH + 'test/weight-staging/weight',
  'billing': DYNAMIC_PATH + 'test/billing-staging/billing'
}
HEADING_SUCCESS = 'team tests success'
MESSAGE_SUCCESS = 'All tests passed successfully!'
HEADING_FAILURE = 'team tests failure'
MESSAGE_FAILURE = 'Some tests have failed. Please check!'

HEADING_SUCCESS_DEPLOY = 'team deploy success'
MESSAGE_SUCCESS_DEPLOY = 'System has been deployed successfully! System is running and operational.'
HEADING_FAILURE_DEPLOY = 'team deploy failure'
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

SWITCHER_STAGING_WEIGHT=1
SWITCHER_STAGING_BILLING=1
SWITCHER_MAIN_BILLING=1
SWITCHER_MAIN_WEIGHT=1    