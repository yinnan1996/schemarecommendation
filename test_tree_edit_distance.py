import unittest
from tree_edit_distance import similarity

class TestJsonSimilarity(unittest.TestCase):

    def setUp(self):
        """Set up sample JSON objects for testing."""
        self.s1 = {
            "_ord": ["合金成分及热处理制度", "性能1", "性能2"],
            "性能1": {
                "r": False,
                "t": 8,
                "misc": {
                    "_head": [
                        "γ'相溶解温度（℃）", "固相线温度（℃）", "液相线温度（℃）",
                        "密度（g/cm3）", "γ'相体积分数（%）", "Vickers microhardness（Gpa）",
                        "洛氏硬度（HRC）", "维氏硬度（Hv）"
                    ],
                    "密度（g/cm3）": {"r": False, "t": 1, "misc": {}},
                    "维氏硬度（Hv）": {"r": False, "t": 1, "misc": {}},
                    "洛氏硬度（HRC）": {"r": False, "t": 1, "misc": {}},
                    "固相线温度（℃）": {"r": False, "t": 1, "misc": {}},
                    "液相线温度（℃）": {"r": False, "t": 1, "misc": {}},
                    "γ'相体积分数（%）": {"r": False, "t": 1, "misc": {}},
                    "γ'相溶解温度（℃）": {"r": False, "t": 1, "misc": {}},
                    "Vickers microhardness（Gpa）": {"r": False, "t": 1, "misc": {}}
                }
            },
            "性能2": {
                "r": False,
                "t": 8,
                "misc": {
                    "_head": [
                        "γ'相尺寸（nm）", "Lattice misfit（%）", "Tensile test",
                        "Elongation at break（%）", "γ'area fractions Af（%）",
                        "Mean oxide layer thickness"
                    ],
                    "Tensile test": {"r": False, "t": 1, "misc": {}},
                    "γ'相尺寸（nm）": {"r": False, "t": 1, "misc": {}},
                    "Lattice misfit（%）": {"r": False, "t": 1, "misc": {}},
                    "Elongation at break（%）": {"r": False, "t": 1, "misc": {}},
                    "Mean oxide layer thickness": {"r": False, "t": 1, "misc": {}},
                    "γ'area fractions Af（%）": {"r": False, "t": 1, "misc": {}}
                }
            },
            "合金成分及热处理制度": {
                "r": False,
                "t": 8,
                "misc": {
                    "_head": [
                        "合金名称（wt %）", "固溶温度1-1（℃）", "固溶时间1-1（h）",
                        "固溶温度1-2（℃）", "固溶时间1-2（h）", "时效温度（℃）",
                        "时效时间（h）"
                    ],
                    "时效时间（h）": {"r": False, "t": 1, "misc": {}},
                    "时效温度（℃）": {"r": False, "t": 1, "misc": {}},
                    "合金名称（wt %）": {"r": True, "t": 1, "misc": {}},
                    "固溶时间1-1（h）": {"r": False, "t": 1, "misc": {}},
                    "固溶时间1-2（h）": {"r": False, "t": 1, "misc": {}},
                    "固溶温度1-1（℃）": {"r": False, "t": 1, "misc": {}},
                    "固溶温度1-2（℃）": {"r": False, "t": 1, "misc": {}}
                }
            }
        }

        self.s2 = {
            "_ord": ["合金成分及热处理制度", "性能2"],
            "性能2": {
                "r": False,
                "t": 8,
                "misc": {
                    "_head": [
                        "γ'相尺寸（nm）", "Lattice misfit（%）", "Tensile test",
                        "Elongation at break（%）", "γ'area fractions Af（%）",
                        "Mean oxide layer thickness"
                    ],
                    "Tensile test": {"r": False, "t": 1, "misc": {}},
                    "γ'相尺寸（nm）": {"r": False, "t": 1, "misc": {}},
                    "Lattice misfit（%）": {"r": False, "t": 1, "misc": {}},
                    "Elongation at break（%）": {"r": False, "t": 1, "misc": {}},
                    "Mean oxide layer thickness": {"r": False, "t": 1, "misc": {}},
                    "γ'area fractions Af（%）": {"r": False, "t": 1, "misc": {}}
                }
            },
            "合金成分及热处理制度": {
                "r": False,
                "t": 8,
                "misc": {
                    "_head": [
                        "合金名称（wt %）", "固溶温度1-1（℃）", "固溶时间1-1（h）",
                        "固溶温度1-2（℃）", "固溶时间1-2（h）", "时效温度（℃）",
                        "时效时间（h）"
                    ],
                    "时效时间（h）": {"r": False, "t": 1, "misc": {}},
                    "时效温度（℃）": {"r": False, "t": 1, "misc": {}},
                    "合金名称（wt %）": {"r": True, "t": 1, "misc": {}},
                    "固溶时间1-1（h）": {"r": False, "t": 1, "misc": {}},
                    "固溶时间1-2（h）": {"r": False, "t": 1, "misc": {}},
                    "固溶温度1-1（℃）": {"r": False, "t": 1, "misc": {}},
                    "固溶温度1-2（℃）": {"r": False, "t": 1, "misc": {}}
                }
            }
        }

    def test_similarity_identical_structures(self):
        """Test similarity of two identical JSON structures."""
        self.assertAlmostEqual(similarity(self.s1, self.s1), 1.0)

    def test_similarity_partial_match(self):
        """Test similarity of JSON structures with partial matches."""
        self.assertGreater(similarity(self.s1, self.s2), 0)

    def test_similarity_no_match(self):
        """Test similarity of JSON structures with no matches."""
        s3 = {"key": "value"}
        self.assertLess(similarity(self.s1, s3), 0.1)

if __name__ == '__main__':
    unittest.main()