# -*- coding:utf-8 -*-
import re
import xlrd
import traceback
import math

def similarity(list1, list2):
    all_set = set(list1) | set(list2)
    list1_map = {}
    for s in list1:
        if s in list1_map:
            list1_map[s] += 1
        else:
            list1_map[s] = 1
    list2_map = {}
    for s in list2:
        if s in list2_map:
            list2_map[s] += 1
        else:
            list2_map[s] = 1
    list1_vec = []
    list2_vec = []
    for s in all_set:
        if s in list1_map:
            list1_vec.append(list1_map[s])
        else:
            list1_vec.append(0)

        if s in list2_map:
            list2_vec.append(list2_map[s])
        else:
            list2_vec.append(0)
    norm1 = math.sqrt(sum(list(map(lambda x: math.pow(x, 2), list1_vec))))
    norm2 = math.sqrt(sum(list(map(lambda x: math.pow(x, 2), list2_vec))))
    if norm1 * norm2 == 0:
        # print(list1, list2)
        return 0
    cos = sum([list1_vec[i]*list2_vec[i] for i in range(0, len(list1_vec))]) / (norm1 * norm2)
    return cos

        




if __name__ == '__main__':
    # print(similarity(['材料牌号', '性能信息', '数据生产与审核', '标准', '加工工艺', '备注'], ['材料牌号', '性能信息', '数据生产与审核', '标准', '加工工艺', '备注']))
    # exit(0)
    wb = xlrd.open_workbook(r"排序筛选的模板片段.xlsx")
    sh2 = wb.sheet_by_index(1)
    cols_content = sh2.col_values(6)
    cols_id = sh2.col_values(0)
    print(len(cols_content))
    template_ord_map = {}
    for i in range(len(cols_id)):
        id = cols_id[i]
        content = cols_content[i]
        ord = re.search(r"{\"_ord\"[:：][ ]\[(.*?)\]", content)
        if ord is not None and ord.lastindex == 1:
            ord_str = ord.group(1)
            ord_str = ord_str.replace("\"", "")
            ord_str = ord_str.replace(" ", "")
            ord_list = ord_str.split(",")
            # print(ord_list)
            template_ord_map[id] = ord_list
    del_list = ["化学成分","基本信息","性能","合金成分","材料牌号","材料成分","试样信息","力学性能","实验条件","实验方法","加工工艺","工艺","材料基本信息","制备工艺","制备方法","热处理工艺","计算结果","管理信息","数据来源","测试条件","类别","数据生产与审核","图片","试验条件","KPOINTS","样品信息","基础信息","润湿性测试数据","工艺参数","涂层厚度","性能信息","纤维预制体参数","增强纤维性能参数","界面厚度及含量","材料热处理","试验图像","材料类别","材料组成成分","材料信息","性能测试","表征过程信息","表征结果信息","性能测试条件","材料表征","表征管理信息","靶材关联参数","非靶材关联参数","POTCAR","测量参数","参考文献","催化材料","测试材料信息","实验数据","数据录入者"]
    xunlian_data = {}
    for k, v in template_ord_map.items():
        res_set = set(v) - set(del_list)
        # template_ord_map[k] = list(res_set)
        if len(set(v)) != len(res_set):
            xunlian_data[k] = list(res_set)
    # print(xunlian_data)

    excel_res = ""
    for k, v in xunlian_data.items():
        similarity_map = {}
        for i, j in template_ord_map.items():
            similarity_map[i] = similarity(v, j)
        res = sorted(similarity_map.items(),key=lambda x:x[1],reverse=True)
        excel_res += ",".join(v)
        excel_res += "\t"
        top5_ord = []
        top5_sim = []
        for i in res[:5]:
            # top5_ord.append(template_ord_map[int(i[0])].join(","))
            excel_res += i[0]
            excel_res += ":"
            excel_res += str(i[1])
            excel_res += ","
        excel_res = excel_res[:len(excel_res)-1]
        # excel_res += top5_ord.join("\n")
        excel_res += "\t"
        xifen_map = {}
        for i in res[:5]:
            ord = template_ord_map[i[0]]
            r = set(ord) - set(v)
            for rr in r:
                if rr in xifen_map:
                    xifen_map[rr] += 1
                else:
                    xifen_map[rr] = 1
            excel_res += '[' + ",".join(r) + ']'
            excel_res += ','
        xifen_res = sorted(xifen_map.items(),key=lambda x:x[1],reverse=True)
        excel_res = excel_res[:len(excel_res)-1]
        excel_res += '\t'
        excel_res += str(xifen_res)
        excel_res += '\t'
        excel_res += '[' + ",".join(template_ord_map[k]) + ']'
        excel_res += "\t"
        for i in res[:5]:
            excel_res += i[0]
            excel_res += ":"
            excel_res += '[' + ",".join(template_ord_map[i[0]]) + ']'
            excel_res += ","
        excel_res = excel_res[:len(excel_res)-1]
        excel_res += '\n'
    
    with open(r'test5.txt', 'w', encoding = "utf-8") as f:      #/会被转义，加r
        f.write(excel_res)


