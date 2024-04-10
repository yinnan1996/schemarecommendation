# -*- coding: UTF-8 -*- 
import str2json
import json2tree
from apted import APTED, helpers


def similarity(sj1, sj2):
    # sj1 = str2json.str2json(s1)
    # sj2 = str2json.str2json(s2)

    root1 = json2tree.json2tree(sj1, None)
    root2 = json2tree.json2tree(sj2, None)

    stree1 = json2tree.json2kuohao(root1)
    stree2 = json2tree.json2kuohao(root2)

    tree1 = helpers.Tree.from_text(stree1)
    tree2 = helpers.Tree.from_text(stree2)

    apted = APTED(tree1, tree2)
    ted = apted.compute_edit_distance()
    # print(ted)
    mapping = apted.compute_edit_mapping()
    # print(mapping)

    # num_tree1node+num_tree2node-TED
    # similarity = stree1.count("{") + stree2.count("{") - ted
    similarity = 1 - (ted / max(stree1.count("{"), stree2.count("{")))
    # print(similarity)
    return similarity


s1 =  """{"_ord": ["合金成分及热处理制度", "性能1", "性能2"], "性能1": {"r": false, "t": 8, "misc": {"_head": ["γ'相溶解温度（℃）", "固相线温度（℃）", "液相线温度（℃）", "密度（g/cm3）", "γ'相体积分数（%）", "Vickers microhardness（Gpa）", "洛氏硬度（HRC）", "维氏硬度（Hv）"], "密度（g/cm3）": {"r": false, "t": 1, "misc": {}}, "维氏硬度（Hv）": {"r": false, "t": 1, "misc": {}}, "洛氏硬度（HRC）": {"r": false, "t": 1, "misc": {}}, "固相线温度（℃）": {"r": false, "t": 1, "misc": {}}, "液相线温度（℃）": {"r": false, "t": 1, "misc": {}}, "γ'相体积分数（%）": {"r": false, "t": 1, "misc": {}}, "γ'相溶解温度（℃）": {"r": false, "t": 1, "misc": {}}, "Vickers microhardness（Gpa）": {"r": false, "t": 1, "misc": {}}}}, "性能2": {"r": false, "t": 8, "misc": {"_head": ["γ'相尺寸（nm）", "Lattice misfit（%）", "Tensile test", "Elongation at break（%）", "γ'area fractions Af（%）", "Mean oxide layer thickness"], "Tensile test": {"r": false, "t": 1, "misc": {}}, "γ'相尺寸（nm）": {"r": false, "t": 1, "misc": {}}, "Lattice misfit（%）": {"r": false, "t": 1, "misc": {}}, "Elongation at break（%）": {"r": false, "t": 1, "misc": {}}, "Mean oxide layer thickness": {"r": false, "t": 1, "misc": {}}, "γ'area fractions Af（%）": {"r": false, "t": 1, "misc": {}}}}, "合金成分及热处理制度": {"r": false, "t": 8, "misc": {"_head": ["合金名称（wt %）", "固溶温度1-1（℃）", "固溶时间1-1（h）", "固溶温度1-2（℃）", "固溶时间1-2（h）", "时效温度（℃）", "时效时间（h）"], "时效时间（h）": {"r": false, "t": 1, "misc": {}}, "时效温度（℃）": {"r": false, "t": 1, "misc": {}}, "合金名称（wt %）": {"r": true, "t": 1, "misc": {}}, "固溶时间1-1（h）": {"r": false, "t": 1, "misc": {}}, "固溶时间1-2（h）": {"r": false, "t": 1, "misc": {}}, "固溶温度1-1（℃）": {"r": false, "t": 1, "misc": {}}, "固溶温度1-2（℃）": {"r": false, "t": 1, "misc": {}}}}}
"""

s2 = """{"_ord": ["合金成分及热处理制度","性能2"], "性能2": {"r": false, "t": 8, "misc": {"_head": ["γ'相尺寸（nm）", "Lattice misfit（%）", "Tensile test", "Elongation at break（%）", "γ'area fractions Af（%）", "Mean oxide layer thickness"], "Tensile test": {"r": false, "t": 1, "misc": {}}, "γ'相尺寸（nm）": {"r": false, "t": 1, "misc": {}}, "Lattice misfit（%）": {"r": false, "t": 1, "misc": {}}, "Elongation at break（%）": {"r": false, "t": 1, "misc": {}}, "Mean oxide layer thickness": {"r": false, "t": 1, "misc": {}}, "γ'area fractions Af（%）": {"r": false, "t": 1, "misc": {}}}}, "合金成分及热处理制度": {"r": false, "t": 8, "misc": {"_head": ["合金名称（wt %）", "固溶温度1-1（℃）", "固溶时间1-1（h）", "固溶温度1-2（℃）", "固溶时间1-2（h）", "时效温度（℃）", "时效时间（h）"], "时效时间（h）": {"r": false, "t": 1, "misc": {}}, "时效温度（℃）": {"r": false, "t": 1, "misc": {}}, "合金名称（wt %）": {"r": true, "t": 1, "misc": {}}, "固溶时间1-1（h）": {"r": false, "t": 1, "misc": {}}, "固溶时间1-2（h）": {"r": false, "t": 1, "misc": {}}, "固溶温度1-1（℃）": {"r": false, "t": 1, "misc": {}}, "固溶温度1-2（℃）": {"r": false, "t": 1, "misc": {}}}}}
"""
# s = """

# """




