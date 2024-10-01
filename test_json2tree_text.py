import unittest
from json2tree_text import json2tree, tree2text, Node

class TestJsonTreeConversion(unittest.TestCase):

    def setUp(self):
        """Set up a sample JSON object for testing."""
        self.sample_json = {
            "1": {
                "2": 2,
                "3": {
                    "4": 4,
                    "5": 0
                }
            }
        }
        self.root_node = json2tree(self.sample_json)

    def test_json2tree_structure(self):
        """Test the structure of the tree created from JSON."""
        self.assertEqual(self.root_node.label, "root")
        self.assertEqual(len(self.root_node.children), 1)
        self.assertEqual(self.root_node.children[0].label, "1")
        self.assertEqual(len(self.root_node.children[0].children), 2)

    def test_tree2text_conversion(self):
        """Test the conversion of the tree structure back to text."""
        expected_output = "{{1{2}{3{4}{5}}}}"
        self.assertEqual(tree2text(self.root_node), expected_output)

    def test_tree2text_empty_node(self):
        """Test the tree to text conversion with an empty node."""
        empty_node = Node(1, "empty", None, None, [], 0)
        self.assertEqual(tree2text(empty_node), "{}")

    def test_json2tree_leaf_node(self):
        """Test that leaf nodes are correctly identified in the tree."""
        leaf_node = self.root_node.children[0].children[1]
        self.assertEqual(leaf_node.label, "3")
        self.assertEqual(len(leaf_node.children), 2)  # Should have 2 children (4 and 5)

if __name__ == '__main__':
    unittest.main()