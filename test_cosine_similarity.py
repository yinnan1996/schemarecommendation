import unittest
from cosine_similarity import similarity_list, similarity 

class TestSimilarityFunctions(unittest.TestCase):

    def test_similarity_list_identical(self):
        """Test that two identical lists return a similarity of 1.0."""
        list1 = ['a', 'b', 'c']
        list2 = ['a', 'b', 'c']
        self.assertAlmostEqual(similarity_list(list1, list2), 1.0)

    def test_similarity_list_partial_match(self):
        """Test that two lists with some common elements return a similarity greater than 0."""
        list1 = ['a', 'b', 'c']
        list2 = ['a', 'b', 'd']
        self.assertGreater(similarity_list(list1, list2), 0)

    def test_similarity_list_no_match(self):
        """Test that two completely dissimilar lists return a similarity of 0."""
        list1 = ['a', 'b']
        list2 = ['c', 'd']
        self.assertEqual(similarity_list(list1, list2), 0)

    def test_similarity_list_empty(self):
        """Test that two empty lists return a similarity of 0."""
        list1 = []
        list2 = []
        self.assertEqual(similarity_list(list1, list2), 0)

    def test_similarity_list_one_empty(self):
        """Test that one empty list and one non-empty list return a similarity of 0."""
        list1 = ['a', 'b']
        list2 = []
        self.assertEqual(similarity_list(list1, list2), 0)

    def test_similarity_json_similarity(self):
        """Test that JSON objects with some common elements return a similarity greater than 0."""
        data1 = {"_ord": ['a', 'b', 'c']}
        data2 = {"_ord": ['a', 'b', 'd']}
        self.assertGreater(similarity(data1, data2), 0)

    def test_similarity_json_identical(self):
        """Test that two identical JSON objects return a similarity of 1.0."""
        data1 = {"_ord": ['a', 'b', 'c']}
        data2 = {"_ord": ['a', 'b', 'c']}
        self.assertAlmostEqual(similarity(data1, data2), 1.0)

if __name__ == '__main__':
    unittest.main()