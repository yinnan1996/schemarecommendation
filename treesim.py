# -*- coding:utf-8 -*-
import re
import xlrd
import traceback
import math
import json
import copy
import cont_simlarity
import treeEditDistance
import time

del_list = ["化学成分", "基本信息", "性能", "合金成分", "材料牌号", "材料成分", "试样信息", "力学性能", "实验条件", "实验方法", "加工工艺", "工艺", "材料基本信息",
            "制备工艺", "制备方法", "热处理工艺", "计算结果", "管理信息", "数据来源", "测试条件", "类别", "数据生产与审核", "图片", "试验条件", "KPOINTS", "样品信息",
            "基础信息", "润湿性测试数据", "工艺参数", "涂层厚度", "性能信息", "纤维预制体参数", "增强纤维性能参数", "界面厚度及含量", "材料热处理", "试验图像", "材料类别",
            "材料组成成分", "材料信息", "性能测试", "表征过程信息", "表征结果信息", "性能测试条件", "材料表征", "表征管理信息", "靶材关联参数", "非靶材关联参数", "POTCAR",
            "测量参数", "参考文献", "催化材料", "测试材料信息", "实验数据", "数据录入者"]


def similarity():
    pass


if __name__ == '__main__':
    # print(similarity(['材料牌号', '性能信息', '数据生产与审核', '标准', '加工工艺', '备注'], ['材料牌号', '性能信息', '数据生产与审核', '标准', '加工工艺', '备注']))
    # exit(0)
    wb = xlrd.open_workbook(r"排序筛选的模板片段.xlsx")
    sh2 = wb.sheet_by_index(1)
    cols_content = sh2.col_values(6)
    cols_id = sh2.col_values(0)
    test_data = {}
    all_data = {}
    all_data_content = {}
    index = {}
    for i in range(1, len(cols_content)):
        content = cols_content[i]
        id = cols_id[i]
        try:
            content_dict = json.loads(content)
            all_data[id] = copy.deepcopy(content_dict)
            all_data_content[id] = content
            ord = content_dict["_ord"]

            # 添加索引
            for o in ord:
                if o in index:
                    index.get(o).add(id)
                else:
                    index[o] = set()
                    index[o].add(id)

            flag = False
            for dl in del_list:
                if dl in ord:
                    flag = True
                    ord.remove(dl)
                    del content_dict[dl]
            content_dict["_ord"] = ord
            if flag:
                test_data[id] = copy.deepcopy(content_dict)
                if len(test_data) == 100:
                    break
        except:
            print(traceback.format_exc())
            pass
    print("len(test_data):", len(test_data))
    print("len(index):", len(index))
    td_sim_map = {}
    ts = time.time()
    cnt = 1
    for i, td in test_data.items():
        # print("第{}个, 共{}个, 耗时{}".format(cnt, len(test_data.keys()), time.time()-ts))
        start = time.time()
        try:
            td_ord = td["_ord"]
            # print(td_ord)
            td_sim_map[i] = {}
            # 不用索引
            temp_data = all_data
            # 用索引
            index_find_data = {}
            for to in td_ord:
                if to in index:
                    for id in index.get(to):
                        index_find_data[id] = all_data[id]
            temp_data = index_find_data
            for k, ad in temp_data.items():
                ad_ord = ad["_ord"]
                cont_sim = cont_simlarity.similarity(td_ord, ad_ord)
                if cont_sim < 0.2:  #if cont_sim < 0.2:
                    tree_sim = 0
                else:
                    # n = time.time()
                    tree_sim = treeEditDistance.similarity(td, ad)
                    # print(time.time() - n)
                sim = 0.5 * cont_sim + 0.5 * tree_sim
                # sim = 1
                td_sim_map[i][k] = sim

        except:
            pass
        end = time.time()
        print("第{}个, 耗时{}秒".format(cnt, end - start))
        cnt += 1
        if cnt >= 5:
            break
    excel_res = ""
    for id, v in td_sim_map.items():
        try:
            excel_res += (all_data_content[id]) + "\t"
            excel_res += ','.join(test_data[id]["_ord"]) + "\t"
            top5 = sorted(v.items(), key=lambda x:x[1], reverse=True)[:5]
            excel_res += str(top5)
            excel_res += "\t"
            for t in top5:
                t_id = t[0]
                t_ord = all_data[t_id]["_ord"]
                set_ord = set(t_ord) - set(test_data[id]["_ord"])

                excel_res += "["
                excel_res += ','.join(set_ord)
                excel_res += "]"
            excel_res += "\n"
            # excel_res += ','.join(all_data[id]["_ord"]) + "\n"
        except:
            pass
    # print(excel_res)
    # with open(r'test7v2.txt', 'w', encoding = "utf-8") as f:      #/会被转义，加r
    #     f.write(excel_res)


