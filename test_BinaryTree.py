"""
"""
from BinaryTree import BinaryTree
from BinaryTree import Node
import unittest

class TestNode(unittest.TestCase):
	def setUp(self):
		# sets up object to be tested
		self.node = Node('A')
	# END setUp

    def test_is_parent(self):
		self.assertFalse(self.node.is_parent)
		self.node.add_left_child(Node('B'))
		self.assertTrue(self.node.is_parent)
	# END test_is_parent

    def test_add_left_child(self):
		self.assertFalse(self.node.left_child)
		self.node.add_left_child(Node('B'))
		self.assertEqual(self.node.left_child, Node('B'))
	# END test_add_left_child

    def test_add_right_child(self):
		self.assertFalse(self.node.right_child)
		self.node.add_right_child(Node('C'))
		self.assertEqual(self.node.right_child, Node('C'))
	# END test_add_right_child
# END TestNode


class TestBinaryTree(unittest.TestCase):
	def setUp(self):
		# sets up object to be tested

	# END setUp

    def test_init(self):
	# END test_init

    def test_contains(self):
	# END test_contains

    def test_find_LCA(self):
	# END test_find_LCA

	def test_find_LCA_invalid(self):
	# END test_find_LCA_invalid

	def test_find_LCA_self(self):
	# END test_find_LCA_self

	def test_find_LCA_same(self):
	# END test_find_LCA_same
# END TestBinaryTree
