import xlrd
import re

if __name__ == '__main__':
    wb = xlrd.open_workbook("D:\document\code\doctor\schemarec\preprocess\排序筛选的模板片段2.xlsx")
    sh3 = wb.sheet_by_index(4)
    standard_schema_fragments_all = sh3.col_values(0)
    standard_schema_fragments_cnt = sh3.col_values(1)

    standard_schema_fragments = []
    for i, c in enumerate(standard_schema_fragments_cnt):
        if c != '频次' and c >= 5:
            standard_schema_fragments.append(standard_schema_fragments_all[i])
    print(standard_schema_fragments)
    ns_recommendation = []

    total = 0
    sh1 = wb.sheet_by_index(1)
    contents = sh1.col_values(6)
    for content in contents:
        ord = re.search(r"{\"_ord\"[:：][ ]\[(.*?)\]", content)
        if ord is not None and ord.lastindex == 1:
            ord_str = ord.group(1)
            ord_str = ord_str.replace("\"", "")
            ord_str = ord_str.replace(" ", "")
            ord_list = ord_str.split(",")
            cnt = 0
            for o in ord_list:
                if o in standard_schema_fragments:
                    cnt += 1
            if cnt / len(ord_list) > 0.8:
                ns_recommendation.append(content)
            if cnt / len(ord_list) > 0:
                total += 1
    print(len(ns_recommendation))
    print(total)
    print(len(ns_recommendation)/total)
