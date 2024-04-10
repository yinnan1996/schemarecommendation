# -*- coding: UTF-8 -*- 
import json
import pprint

def str2json(s):
    """
    {"_ord": ["合金成分及热处理制度", "性能1", "性能2"], "性能1": {"r": false, "t": 8, "misc": {"_head": ["γ'相溶解温度（℃）", "固相线温度（℃）", "液相线温度（℃）", "密度（g/cm3）", "γ'相体积分数（%）", "Vickers microhardness（Gpa）", "洛氏硬度（HRC）", "维氏硬度（Hv）"], "密度（g/cm3）": {"r": false, "t": 1, "misc": {}}, "维氏硬度（Hv）": {"r": false, "t": 1, "misc": {}}, "洛氏硬度（HRC）": {"r": false, "t": 1, "misc": {}}, "固相线温度（℃）": {"r": false, "t": 1, "misc": {}}, "液相线温度（℃）": {"r": false, "t": 1, "misc": {}}, "γ'相体积分数（%）": {"r": false, "t": 1, "misc": {}}, "γ'相溶解温度（℃）": {"r": false, "t": 1, "misc": {}}, "Vickers microhardness（Gpa）": {"r": false, "t": 1, "misc": {}}}}, "性能2": {"r": false, "t": 8, "misc": {"_head": ["γ'相尺寸（nm）", "Lattice misfit（%）", "Tensile test", "Elongation at break（%）", "γ'area fractions Af（%）", "Mean oxide layer thickness"], "Tensile test": {"r": false, "t": 1, "misc": {}}, "γ'相尺寸（nm）": {"r": false, "t": 1, "misc": {}}, "Lattice misfit（%）": {"r": false, "t": 1, "misc": {}}, "Elongation at break（%）": {"r": false, "t": 1, "misc": {}}, "Mean oxide layer thickness": {"r": false, "t": 1, "misc": {}}, "γ'area fractions Af（%）": {"r": false, "t": 1, "misc": {}}}}, "合金成分及热处理制度": {"r": false, "t": 8, "misc": {"_head": ["合金名称（wt %）", "固溶温度1-1（℃）", "固溶时间1-1（h）", "固溶温度1-2（℃）", "固溶时间1-2（h）", "时效温度（℃）", "时效时间（h）"], "时效时间（h）": {"r": false, "t": 1, "misc": {}}, "时效温度（℃）": {"r": false, "t": 1, "misc": {}}, "合金名称（wt %）": {"r": true, "t": 1, "misc": {}}, "固溶时间1-1（h）": {"r": false, "t": 1, "misc": {}}, "固溶时间1-2（h）": {"r": false, "t": 1, "misc": {}}, "固溶温度1-1（℃）": {"r": false, "t": 1, "misc": {}}, "固溶温度1-2（℃）": {"r": false, "t": 1, "misc": {}}}}}
    """
    j = json.loads(s)
    # pprint.pprint(j)
    return j



if __name__ == '__main__':
    s = """
    {"_ord": ["合金成分及热处理制度", "性能1", "性能2"], "性能1": {"r": false, "t": 8, "misc": {"_head": ["γ'相溶解温度（℃）", "固相线温度（℃）", "液相线温度（℃）", "密度（g/cm3）", "γ'相体积分数（%）", "Vickers microhardness（Gpa）", "洛氏硬度（HRC）", "维氏硬度（Hv）"], "密度（g/cm3）": {"r": false, "t": 1, "misc": {}}, "维氏硬度（Hv）": {"r": false, "t": 1, "misc": {}}, "洛氏硬度（HRC）": {"r": false, "t": 1, "misc": {}}, "固相线温度（℃）": {"r": false, "t": 1, "misc": {}}, "液相线温度（℃）": {"r": false, "t": 1, "misc": {}}, "γ'相体积分数（%）": {"r": false, "t": 1, "misc": {}}, "γ'相溶解温度（℃）": {"r": false, "t": 1, "misc": {}}, "Vickers microhardness（Gpa）": {"r": false, "t": 1, "misc": {}}}}, "性能2": {"r": false, "t": 8, "misc": {"_head": ["γ'相尺寸（nm）", "Lattice misfit（%）", "Tensile test", "Elongation at break（%）", "γ'area fractions Af（%）", "Mean oxide layer thickness"], "Tensile test": {"r": false, "t": 1, "misc": {}}, "γ'相尺寸（nm）": {"r": false, "t": 1, "misc": {}}, "Lattice misfit（%）": {"r": false, "t": 1, "misc": {}}, "Elongation at break（%）": {"r": false, "t": 1, "misc": {}}, "Mean oxide layer thickness": {"r": false, "t": 1, "misc": {}}, "γ'area fractions Af（%）": {"r": false, "t": 1, "misc": {}}}}, "合金成分及热处理制度": {"r": false, "t": 8, "misc": {"_head": ["合金名称（wt %）", "固溶温度1-1（℃）", "固溶时间1-1（h）", "固溶温度1-2（℃）", "固溶时间1-2（h）", "时效温度（℃）", "时效时间（h）"], "时效时间（h）": {"r": false, "t": 1, "misc": {}}, "时效温度（℃）": {"r": false, "t": 1, "misc": {}}, "合金名称（wt %）": {"r": true, "t": 1, "misc": {}}, "固溶时间1-1（h）": {"r": false, "t": 1, "misc": {}}, "固溶时间1-2（h）": {"r": false, "t": 1, "misc": {}}, "固溶温度1-1（℃）": {"r": false, "t": 1, "misc": {}}, "固溶温度1-2（℃）": {"r": false, "t": 1, "misc": {}}}}}
    """
    str2json(s)