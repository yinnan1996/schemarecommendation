# -*- coding: UTF-8 -*- 
import xlrd
import str2json
import traceback

def read_and_process_excel(file_name):
    wb = xlrd.open_workbook(file_name)
    sh1 = wb.sheet_by_index(0)
    cols_content = sh1.col_values(6)
    res = []
    for i in range(1, len(cols_content)):
        try:
            r = str2json.str2json(cols_content[i])
            res.append(r)
        except:
            print(traceback.format_exc())
    return res

if __name__ == '__main__':
    read_and_process_excel(r"C:\Users\zjh\Desktop\新建文件夹\b.xlsx")