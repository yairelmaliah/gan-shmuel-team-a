import requests
import sys

def test_health():
  req = requests.get("http://localhost:8081/health")
  status_code = req.status_code
  if (status_code < 200 or status_code > 299): return 0
  else: return 1
  
def test_get_unknown():
  req = requests.get("http://localhost:8081/unknown")
  status_code = req.status_code
  if (status_code < 200 or status_code > 299): return 0
  else: return 1

def test_get_item():
  req = requests.get("http://localhost:8081/item/1234?from=000000000000")
  status_code = req.status_code
  if (status_code < 200 or status_code > 299): return 0
  else: return 1

def test_batch_weight():
  req = requests.post("http://localhost:8081/batch-weight/containers3.json")
  status_code = req.status_code
  if (status_code < 200 or status_code > 299): 
    return 0
  else: return 1

def test_get_weight():
  req = requests.get("http://localhost:8081/weight")
  status_code = req.status_code
  if (status_code < 200 or status_code > 299): return 0
  else: return 1

def test():
  functions = [test_health, test_get_unknown, test_get_item, test_batch_weight, test_get_weight]
  for func in functions:
    if not func():
      sys.exit(0)

  sys.exit(1)


if __name__ == '__main__':
  try:
    test()
  except Exception as e:
    sys.exit(0)
    print(f"SERVER ERROR!!!")

