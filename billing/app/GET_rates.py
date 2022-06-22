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
    return ("Your Newest rates is in your /in file in the name : last_rate_file.xlsx" , 200)

    
if __name__ == '__main__':
    GET_rates()


    # if request.method == 'GET':
    #     output_dir = os.path.join('app', 'downloads')
    #     data = helper.get_all(Rate)
    #     wb = Workbook()
    #     ws = wb.active
    #     if not os.path.isdir(output_dir):
    #         os.mkdir(output_dir)
    #     headers = ['Product', 'Rate', 'Scope']
    #     for col_num, header in enumerate(headers):
    #         ws.cell(row=1, column=col_num + 1).value = header
    #     for row_num, row in enumerate(data):
    #         real_row_num = row_num + 2
    #         ws.cell(row=real_row_num, column=1).value = row.product_name
    #         ws.cell(row=real_row_num, column=2).value = row.rate
    #         ws.cell(row=real_row_num, column=3).value = row.scope

    #     # wb.save(os.path.join(output_dir, output_file))
    #     # print(os.getcwd())
    #     #------------------
    #     return Response(save_virtual_workbook(wb), headers={'Content-Disposition': 'attachment; filename=rates.xlsx',
    #                                                        'Content-type': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    #                                                        })