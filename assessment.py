from copy import copy

import xlrd
import traceback
import re


def accurency():
    wb = xlrd.open_workbook('D:\document\code\doctor\schemarec\preprocess\排序筛选的模板片段2.xlsx')
    sh1 = wb.sheet_by_index(4)
    schema_sims = sh1.col_values(1)
    print("schema_sims",schema_sims)
    fragments = sh1.col_values(2)
    res_map = {}
    for i in range(1, len(schema_sims)):
        schema_sim_list = schema_sims[i].split(',')
        fragment_list = fragments[i].split('],[')
        # print(schema_sim_list)schema_sim_list
        # print(fragment_list)
        fragment_map = {}
        for idx, fragment_raw in enumerate(fragment_list):
            schema_sim_raw = schema_sim_list[idx]
            match = re.match(r"\d+:(\S+)", schema_sim_raw)
            if match:
                schema_sim = float(match.group(1))
            else:
                schema_sim = 0
            fragment_seq = fragment_raw.replace('[', '').replace(']', '').split(',')
            for fragment in fragment_seq:
                if fragment:
                    if fragment not in fragment_map:
                        fragment_map[fragment] = schema_sim
                    else:
                        fragment_map[fragment] = fragment_map[fragment] + schema_sim
        # res_map[i] = fragment_map
        topN = sorted(fragment_map.items(), key=lambda x: x[1], reverse=True)
        res_map[i] = topN

    excel_res = ''
    for row, res in res_map.items():
        excel_res += str(res)
        excel_res += '\n'
    # with open(r'test8.txt', 'w', encoding = "utf-8") as f:      #/会被转义，加r
    #     f.write(excel_res)

    raw_templates = sh1.col_values(4)
    test_template = sh1.col_values(0)
    # print(raw_templates)raw_templates

    accurency_count_map = {}
    expect_accurency_count_map = {}
    k = 10
    print("推荐片段个数：",k)
    for i in range(1, 10):
        accurency_count_map[i] = 0
        raw_template_list = raw_templates[i].replace('[', '').replace(']', '').split(',')
        # print(test_template[i])
        # print(len(test_template[i].split(',')))
        expect_accurency_count_map[i] = len(raw_template_list) - len(test_template[i].split(','))
        topk = res_map[i][:k]
        for j in topk:
            if j[0] in raw_template_list:
                accurency_count_map[i] += 1
    accurency_count = 0
    total = 0

    for row, count in accurency_count_map.items():
        accurency_count += count
        if test_template[row]:
            total += k

    expect_accurency_count = 0
    for row, count in expect_accurency_count_map.items():
        expect_accurency_count += count

    return accurency_count, total, expect_accurency_count

def precision(accurency_count, total):
    return accurency_count / total


def relevance(accurency_count, expect_accurency_count):
    return accurency_count / expect_accurency_count

def f1(precision, relevance):
    return (precision * relevance * 2) / (precision + relevance)

if __name__ == '__main__':
    # assessment()assessment
    accurent_count, total, expect_accurency_count = accurency()
    p = precision(accurent_count, total)
    r = relevance(accurent_count, expect_accurency_count)
    print("精确率：",precision(accurent_count, total))
    print("召回率：",relevance(accurent_count, expect_accurency_count))
    print(f1(p, r))