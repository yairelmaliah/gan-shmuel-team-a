import os
def run_test(branch_name):
  os.system(f'docker-compose -f /tmp/gan-shmuel-app/{branch_name}/docker-compose.yaml down ')
  os.system(f'docker-compose -f /tmp/gan-shmuel-app/{branch_name}/docker-compose.yaml up -d')
  if branch_name == "billing":
    return os.system(f'python3 /tmp/gan-shmuel-app/{branch_name}/app/testing.py')
  else:
    return os.system(f'python3 /tmp/gan-shmuel-app/{branch_name}/app/test.py')

  



# def run_app(branch_name):


  