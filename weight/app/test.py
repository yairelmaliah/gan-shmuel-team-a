import requests

def test_health():
  req = requests.get("http://localhost:8081/health")
  status_code = req.status_code
  if (status_code < 200 or status_code > 299): return 0
  else: return 1
  
def test_get_unknown():
  req = requests.get("http://localhost:8081/get_unknown")
  status_code = req.status_code
  if (status_code < 200 or status_code > 299): return 0
  else: return 1

def test_get_item():
  req = requests.get("http://localhost:8081/get_item/1234?from=000000000000")
  status_code = req.status_code
  if (status_code < 200 or status_code > 299): return 0
  else: return 1

def test_batch_weight():
  req = requests.get("http://localhost:8081/batch_weight/containers3.json")
  status_code = req.status_code
  if (status_code < 200 or status_code > 299): return 0
  else: return 1

def test_get_weight():
  req = requests.get("http://localhost:8081/get_weight")
  status_code = req.status_code
  if (status_code < 200 or status_code > 299): return 0
  else: return 1

if __name__ == '__main__':
  if test_health() and test_get_unknown() and test_get_item() and test_batch_weight() and test_get_weight():
    print("OK")
  else:
    print("ERROR")