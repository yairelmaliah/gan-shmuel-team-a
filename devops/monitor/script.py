import requests

def checking(checking_result, f):
    if checking_result == 200:
        f.write("opened\n")
    else:
        f.write("closed\n")

def portstatus(dev):
    url = "http://3.66.68.27"
    ports = [8080, 8081, 8082, 8083, 8084]
    ports = [8081]
    if dev:
        url = "http://localhost"
        ports = [3000, 5000]
    open('open_ports.txt', 'w').close()
    f = open('open_ports.txt', 'a')
    
    for p in ports:
        status_code = requests.get(f"{url}:{p}/health").status_code
        checking(status_code, f)
    
    f.close()
    
