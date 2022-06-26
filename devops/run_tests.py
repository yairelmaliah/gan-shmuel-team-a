import os
import subprocess
import time
from config import *

def run_test(branch_name):
  os.system(f'docker-compose -p test-{branch_name} -f {TEST_TMP_PATH}/{branch_name}/docker-compose.test.yaml up --build -d')
  
  print("running tests...", flush=True)
  time.sleep(15)

  if branch_name == "billing":
    return subprocess.check_output(['python3', f'{TEST_TMP_PATH}/{branch_name}/app/testing.py', 'test'])

  if branch_name == "weight":
    return subprocess.check_output(['python3', f'{TEST_TMP_PATH}/{branch_name}/app/test.py', 'test'])
