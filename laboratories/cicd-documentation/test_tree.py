import unittest
from tree import Tree
from node import Node

# Test class for Tree
class TestTree(unittest.TestCase):

    def setUp(self):
        self.tree = Tree()
        for value in [5, 3, 8, 1, 4]:
            self.tree.add(value)

    def test_find_existing_node(self):
        node = self.tree.find(3)
        self.assertIsNotNone(node)
        self.assertEqual(node.data, 3)

    def test_find_non_existing_node(self):
        node = self.tree.find(10)
        self.assertIsNone(node)

if __name__ == '__main__':
    unittest.main()
