import requests
from time import sleep 


def GET_health(url):

      new = ""

      try:
            url = [f'http://3.66.68.27:8080/{url}']
            #Get Url
            get = requests.get(url[0])
            # if the request succeeds 
            if get.status_code == 200:
               print(f"{url}: is reachable")
               new = (f"{url}: is reachable")

               #return 1
            else:
               print(f"{url}: is Not reachable, status_code: {get.status_code}")
               new = (f"{url}: is Not reachable, status_code: {get.status_code}")

               #return 0
      

      #Exception
      except requests.exceptions.RequestException as e:
         # print URL with Errs
         raise SystemExit(f"{url}: is Not reachable \nErr: {e}")
      finally:
     
         return new

# def GET_health(url):
#    #  urlname = ['health', 'provider', 'rates', 'truck']
#     for url in urlname:
#         request = requests.get(url)
#       #   print(url)
#         status_code = request.status_code
#         result = ""
#         if status_code >= 200 or status_code < 299:
#            result = f"service on, status code: {status_code}"
#            return result
#         #    print(result)
#         else:
#            result = f"service fail, status code: {status_code}"
#         #    print(result)
#     
#       return result

if __name__ == '__main__':   
   # GET_health()
   #urlname = ['','home', 'provider','rates','truck','not_real_valid']
  # for url in urlname:
    #  sleep(1)
      GET_health(url)
    
