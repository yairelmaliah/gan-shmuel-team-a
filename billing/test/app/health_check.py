from GET_health import GET_health
from time import sleep


def health_check():
    all_data = ""
    urlname = ['home', 'provider','rates','truck','not_real_valid']
    for url in urlname:
        
        all_data += str(GET_health(url))
        sleep(1)

    
    return str(all_data)

if __name__ == '__main__':   
    health_check()
   
   
      
      