import requests
from db_utils import db_utils


mysql = db_utils()



def POST_provider():
    val = "test2"
    data_insert = f"INSERT INTO Provider (name) VALUES ('{val}');"


    mysql.setData(data_insert)
    return mysql.getData(f'select name,id from Provider where name = "{val}"')
    


if __name__ == '__main__':
    POST_provider()    
