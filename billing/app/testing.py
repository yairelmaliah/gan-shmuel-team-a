import requests
from time import sleep
import sys

# Please run the script : "python3 testing.py" in order to check all apis
# *******
# Logs information:
#   - GREEN: everything good and work - the connection should be fine.
#   - ORANGE: everything good, but the data your trying to send is probably already exist in the Database (in this case: status 409 - conflict)
#   - RED: ERROR!: please check, something went wrong with reqeust or connection is failed!
# ******

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

url = ""

if "dev" in sys.argv:
  url = "http://localhost:5000"
if "test" in sys.argv:
  url = "http://3.66.68.27:8084"
if "prod" in sys.argv:
  url = "http://3.66.68.27:8080"
  
if not url:
  sys.stdout.write('You must specify what environment you are in, dev OR test OR prod, eg. "python3 testing.py dev"')
  exit(0)

def test_health():
  req = requests.get(f"{url}/health")
  status_code = req.status_code
  log_name = "HEALTH"
  if (status_code < 200 or status_code > 299): 
    print(f"{bcolors.FAIL}{log_name}ERROR: Oh, Something went wrong!, {bcolors.HEADER}status code: {req}{bcolors.ENDC}")
    return 0
  else: 
    print(f"{bcolors.OKGREEN}HEALTH: OK, {bcolors.HEADER}status code: {req}{bcolors.ENDC}")
    return 1
  
def test_post_provider():
  payload = {'provider':'fgrttt'} # because its send it with form
  log_name = "POST PROVIDER"
  req = requests.post(f"{url}/api/provider", data=payload)
  status_code = req.status_code
  if ((status_code >= 200 and status_code < 299) and status_code != 409): 
    print(f"{bcolors.OKGREEN}{log_name} OK: new provider was inserted into the Database, {bcolors.HEADER}status code: {req}{bcolors.ENDC}")
    return 1
  elif (status_code == 409):
    print(f"{bcolors.WARNING}{log_name}: This name already exist!, {bcolors.HEADER}status code: {req}{bcolors.ENDC}")
    return 1
  else:
    print(f"{bcolors.FAIL}{log_name} ERROR: Oh, Something went wrong!, {bcolors.HEADER}status code: {req}{bcolors.ENDC}")
    return 0

def test_put_provider():
  req = requests.put(f"{url}/api/provider/10001?new_provider=mdagfgda")
  log_name = "PUT(UPDATE) PROVIDER"
  status_code = req.status_code
  if ((status_code >= 200 and status_code < 299) and status_code != 409):
    print(f"{bcolors.OKGREEN}{log_name}: name is changed in the Database, {bcolors.HEADER}status code: {req}{bcolors.ENDC}")
    return 1
  elif (status_code == 409): 
    print(f"{bcolors.WARNING}{log_name}: This name already exist!, {bcolors.HEADER}status code: {req}{bcolors.ENDC}")
    return 1
  else:
    print(f"{bcolors.FAIL}{log_name} ERROR: Oh, Something went wrong!, {bcolors.HEADER}status code: {req}{bcolors.ENDC}")
    return 0

def test_post_truck():
  # req = requests.post(f"{url}/api/truck?provider_id=10009&truck_id=200-10-300")
  payload = {'provider_id':'10009', 'truck_id':'200-10-300'} # because its send it with form
  req = requests.post(f"{url}/api/truck", data=payload)
  log_name = "POST TRUCK"
  status_code = req.status_code
  if ((status_code >= 200 and status_code < 299) and status_code != 409):
    print(f"{bcolors.OKGREEN}{log_name} OK: new truck was inserted into the Database, {bcolors.HEADER}status code: {req}{bcolors.ENDC}")
    return 1
  elif (status_code == 409): 
    print(f"{bcolors.WARNING}{log_name}: Provider not found or truck id already exist, {bcolors.HEADER}status code: {req}{bcolors.ENDC}")
    return 1
  else:
    print(f"{bcolors.FAIL}{log_name} ERROR: Oh, Something went wrong!, {bcolors.HEADER}status code: {req}{bcolors.ENDC}")
    return 0

def test_put_truck():
  payload = {'provider_id':'10001'} # because its send it with form
  req = requests.put(f"{url}/truck/200-10-300", data=payload)
  log_name = "PUT(UPDATE) TRUCK"
  status_code = req.status_code
  if ((status_code >= 200 and status_code < 299) and status_code != 409):
    print(f"{bcolors.OKGREEN}{log_name} OK: provider id is changed in the Database, {bcolors.HEADER}status code: {req}{bcolors.ENDC}")
    return 1
  elif (status_code == 409): 
    print(f"{bcolors.WARNING}{log_name}: Provider not found or truck id already exist, {bcolors.HEADER}status code: {req}{bcolors.ENDC}")
    return 1
  else:
    print(f"{bcolors.FAIL}{log_name} ERROR: Oh, Something went wrong!, {bcolors.HEADER}status code: {req}{bcolors.ENDC}")
    return 0

def test_get_truck():
  req = requests.get(f"{url}/truck/155-34-443?from=20210311203010&to=20230311203010")
  log_name = "GET TRUCK"
  status_code = req.status_code
  if ((status_code >= 200 and status_code < 299) and status_code != 409):
    print(f"{bcolors.OKGREEN}{log_name} OK!, {bcolors.HEADER}status code: {req}{bcolors.ENDC}")
    return 1
  elif (status_code == 409): 
    print(f"{bcolors.WARNING}{log_name}: 'from' or 'to' date is not valid, please try again!, {bcolors.HEADER}status code: {req}{bcolors.ENDC}")
    return 1
  else:
    print(f"{bcolors.FAIL}{log_name} ERROR: Oh, Something went wrong!, {bcolors.HEADER}status code: {req}{bcolors.ENDC}")
    return 0


def test_post_rates():
  req = requests.post(f"{url}/api/rates/rates.xlsx")
  log_name = "POST RATES"
  status_code = req.status_code
  if (status_code < 200 or status_code > 299):
    print(f"{bcolors.FAIL}{log_name} ERROR: Oh, Something went wrong!, {bcolors.HEADER}status code: {req}{bcolors.ENDC}")
    return 0
  else:
    print(f"{bcolors.OKGREEN}{log_name} OK!, {bcolors.HEADER}status code: {req}{bcolors.ENDC}")
    return 1

def test_get_rates():
  req = requests.get(f"{url}/api/rates")
  log_name = "GET RATES"
  status_code = req.status_code
  if (status_code < 200 or status_code > 299):
    print(f"{bcolors.FAIL}{log_name} ERROR: Oh, Something went wrong!, {bcolors.HEADER}status code: {req}{bcolors.ENDC}")
    return 0
  else:
    print(f"{bcolors.OKGREEN}{log_name} OK!, {bcolors.HEADER}status code: {req}{bcolors.ENDC}")
    return 1

def test_get_bill():
  req = requests.get(f"{url}/bill/10002?from=20210311203010&to=20230311203010")
  log_name = "GET BILL"
  status_code = req.status_code
  if (status_code < 200 or status_code > 299):
    print(f"{bcolors.FAIL}{log_name} ERROR: Oh, Something went wrong!, {bcolors.HEADER}status code: {req}{bcolors.ENDC}")
    return 0
  else:
    print(f"{bcolors.OKGREEN}{log_name} OK!, {bcolors.HEADER}status code: {req}{bcolors.ENDC}")
    return 1

 

def test():
  functions = [test_health, test_post_provider, test_put_provider, test_post_truck, test_put_truck, test_get_truck, test_post_rates, test_get_rates, test_get_bill]
  for func in functions:
    if not func():
      sys.stdout.write(f'ERROR ==> {func.__name__}\n')
    sleep(0.17)

  sys.stdout.write('SUCCESS!\n')

if __name__ == '__main__':
  test()
