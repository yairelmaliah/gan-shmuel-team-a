import os
import subprocess
import time

def run_test(branch_name):
  # os.system(f'docker-compose -f /tmp/gan-shmuel-app/{branch_name}/docker-compose.yaml -f /tmp/gan-shmuel-app/{branch_name}/docker-compose.test.yaml down')
  os.system(f'docker-compose -f /tmp/gan-shmuel-app/{branch_name}/docker-compose.test.yaml up --build -d')
  
  print("running tests...", flush=True)
  time.sleep(15)

  if branch_name == "billing":
    return subprocess.check_output(['python3', f'/tmp/gan-shmuel-app/{branch_name}/app/testing.py', 'test'])

  if branch_name == "weight":
    return subprocess.check_output(['python3', f'/tmp/gan-shmuel-app/{branch_name}/app/test.py', 'test'])
