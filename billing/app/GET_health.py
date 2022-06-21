import requests

def GET_health():
    request = requests.get(f"http://localhost:5000")
    status_code = request.status_code
    result = ""
    if status_code >= 200 or status_code < 299:
        result = f"service on, status code: {status_code}"
    else:
        result = f"service fail, status code: {status_code}"

    return result

if __name__ == '__main__':
    GET_health()    
