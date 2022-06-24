import os
import subprocess

def run_test(branch_name):
  # os.system(f'docker-compose -f /tmp/gan-shmuel-app/{branch_name}/docker-compose.yaml -f /tmp/gan-shmuel-app/{branch_name}/docker-compose.test.yaml down')
  os.system(f'docker-compose -f /tmp/gan-shmuel-app/{branch_name}/docker-compose.test.yaml up -d')
  
  # result=subprocess.check_output(['python3', '/tmp/gan-shmuel-app/{branch_name}/app/testing.py'])
  if branch_name == "billing":
    return subprocess.check_output(['python3', f'/tmp/gan-shmuel-app/{branch_name}/app/testing.py'])
    # return os.system(f'python3 /tmp/gan-shmuel-app/{branch_name}/app/testing.py')
  else:
    return subprocess.check_output(['python3', f'/tmp/gan-shmuel-app/{branch_name}/app/test.py'])
    # return os.system(f'python3 /tmp/gan-shmuel-app/{branch_name}/app/test.py')





# def run_app(branch_name):


  