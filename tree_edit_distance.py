# -*- coding: UTF-8 -*- 
import json2tree_text
import json
from apted import APTED, helpers

def similarity(data1, data2):
    """
    Calculate the similarity between two JSON objects using Tree Edit Distance (TED).

    Args:
        data1 (dict): The first JSON object.
        data2 (dict): The second JSON object.

    Returns:
        float: A similarity score between 0 and 1, where 1 indicates identical structures.
    """
    root1 = json2tree_text.json2tree(data1)
    root2 = json2tree_text.json2tree(data2)

    tree_text1 = json2tree_text.tree2text(root1)
    tree_text2 = json2tree_text.tree2text(root2)

    tree1 = helpers.Tree.from_text(tree_text1)
    tree2 = helpers.Tree.from_text(tree_text2)

    apted = APTED(tree1, tree2)
    ted = apted.compute_edit_distance()
    similarity = 1 - (ted / max(tree_text1.count("{"), tree_text2.count("{")))
    return similarity

if __name__ == '__main__':
    s1 =  """{"_ord": ["合金成分及热处理制度", "性能1", "性能2"], "性能1": {"r": false, "t": 8, "misc": {"_head": ["γ'相溶解温度（℃）", "固相线温度（℃）", "液相线温度（℃）", "密度（g/cm3）", "γ'相体积分数（%）", "Vickers microhardness（Gpa）", "洛氏硬度（HRC）", "维氏硬度（Hv）"], "密度（g/cm3）": {"r": false, "t": 1, "misc": {}}, "维氏硬度（Hv）": {"r": false, "t": 1, "misc": {}}, "洛氏硬度（HRC）": {"r": false, "t": 1, "misc": {}}, "固相线温度（℃）": {"r": false, "t": 1, "misc": {}}, "液相线温度（℃）": {"r": false, "t": 1, "misc": {}}, "γ'相体积分数（%）": {"r": false, "t": 1, "misc": {}}, "γ'相溶解温度（℃）": {"r": false, "t": 1, "misc": {}}, "Vickers microhardness（Gpa）": {"r": false, "t": 1, "misc": {}}}}, "性能2": {"r": false, "t": 8, "misc": {"_head": ["γ'相尺寸（nm）", "Lattice misfit（%）", "Tensile test", "Elongation at break（%）", "γ'area fractions Af（%）", "Mean oxide layer thickness"], "Tensile test": {"r": false, "t": 1, "misc": {}}, "γ'相尺寸（nm）": {"r": false, "t": 1, "misc": {}}, "Lattice misfit（%）": {"r": false, "t": 1, "misc": {}}, "Elongation at break（%）": {"r": false, "t": 1, "misc": {}}, "Mean oxide layer thickness": {"r": false, "t": 1, "misc": {}}, "γ'area fractions Af（%）": {"r": false, "t": 1, "misc": {}}}}, "合金成分及热处理制度": {"r": false, "t": 8, "misc": {"_head": ["合金名称（wt %）", "固溶温度1-1（℃）", "固溶时间1-1（h）", "固溶温度1-2（℃）", "固溶时间1-2（h）", "时效温度（℃）", "时效时间（h）"], "时效时间（h）": {"r": false, "t": 1, "misc": {}}, "时效温度（℃）": {"r": false, "t": 1, "misc": {}}, "合金名称（wt %）": {"r": true, "t": 1, "misc": {}}, "固溶时间1-1（h）": {"r": false, "t": 1, "misc": {}}, "固溶时间1-2（h）": {"r": false, "t": 1, "misc": {}}, "固溶温度1-1（℃）": {"r": false, "t": 1, "misc": {}}, "固溶温度1-2（℃）": {"r": false, "t": 1, "misc": {}}}}}
    """
    s2 = """{"_ord": ["合金成分及热处理制度","性能2"], "性能2": {"r": false, "t": 8, "misc": {"_head": ["γ'相尺寸（nm）", "Lattice misfit（%）", "Tensile test", "Elongation at break（%）", "γ'area fractions Af（%）", "Mean oxide layer thickness"], "Tensile test": {"r": false, "t": 1, "misc": {}}, "γ'相尺寸（nm）": {"r": false, "t": 1, "misc": {}}, "Lattice misfit（%）": {"r": false, "t": 1, "misc": {}}, "Elongation at break（%）": {"r": false, "t": 1, "misc": {}}, "Mean oxide layer thickness": {"r": false, "t": 1, "misc": {}}, "γ'area fractions Af（%）": {"r": false, "t": 1, "misc": {}}}}, "合金成分及热处理制度": {"r": false, "t": 8, "misc": {"_head": ["合金名称（wt %）", "固溶温度1-1（℃）", "固溶时间1-1（h）", "固溶温度1-2（℃）", "固溶时间1-2（h）", "时效温度（℃）", "时效时间（h）"], "时效时间（h）": {"r": false, "t": 1, "misc": {}}, "时效温度（℃）": {"r": false, "t": 1, "misc": {}}, "合金名称（wt %）": {"r": true, "t": 1, "misc": {}}, "固溶时间1-1（h）": {"r": false, "t": 1, "misc": {}}, "固溶时间1-2（h）": {"r": false, "t": 1, "misc": {}}, "固溶温度1-1（℃）": {"r": false, "t": 1, "misc": {}}, "固溶温度1-2（℃）": {"r": false, "t": 1, "misc": {}}}}}
    """
    print(similarity(json.loads(s1), json.loads(s2)))





