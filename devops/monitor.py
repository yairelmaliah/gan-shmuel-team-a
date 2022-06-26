from flask import render_template
import requests

def portstatus(dev = ""):
    url = "http://3.66.68.27"
    ports = [8080, 8081, 8082, 8083, 8084]
    if dev:
        url = "http://localhost"
        ports = [3000, 5000]
    
    arr = []
    for p in ports:
        try:
          status_code = requests.get(f"{url}:{p}/health").status_code
          arr.append(f"{status_code}\n")
        except:
          arr.append("500\n")
    with open("/tmp/monitor-health.txt", "w") as f:
      f.writelines(arr)
    return arr