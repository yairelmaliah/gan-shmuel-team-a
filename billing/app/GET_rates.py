from re import X
from flask import Flask, render_template, request
from db_utils import db_utils
from openpyxl import Workbook, load_workbook
import shutil

mysql = db_utils()


def GET_rates():
  
    
    f = open("/src/in/last_file.txt", "r")
    file_name = f.read()
    f.close()


    original = f'/src/in/{file_name}'
    target = r'/src/in/last_rate_file.xlsx'

    shutil.copyfile(original, target)
    return ("Your Newest rates is in your /in directory in the name : last_rate_file.xlsx" , 200)

    
if __name__ == '__main__':
    GET_rates()
