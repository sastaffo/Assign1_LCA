#
#

from BinaryTree import BinaryTree
from BinaryTree import Node
import unittest

class TestNode(unittest.TestCase):
	def setUp(self):
		# sets up object to be tested
		self.node = Node('A')
	# END setUp

	def test_equals(self):
		self.assertTrue(self.node.equals(Node('A')))
		self.assertFalse(self.node.equals(Node('E')))

	def test_is_parent(self):
		self.assertFalse(self.node.is_parent)
		self.node.add_left_child(Node('B'))
		self.assertTrue(self.node.is_parent)
	# END test_is_parent

	def test_add_left_child(self):
		self.assertFalse(self.node.left_child)
		self.node.add_left_child(Node('B'))
		self.assertTrue(self.node.left_child.equals(Node('B')))
	# END test_add_left_child

	def test_add_right_child(self):
		self.assertFalse(self.node.right_child)
		self.node.add_right_child(Node('C'))
		self.assertTrue(self.node.right_child.equals(Node('C')))
	# END test_add_right_child
# END TestNode


class TestBinaryTree(unittest.TestCase):
	def setUp(self):
		# sets up object to be tested
		self.binary_tree = BinaryTree(Node('A'))
		self.binary_tree.head.add_left_child(Node('B'))
		self.binary_tree.head.add_right_child(Node('C'))
		self.binary_tree.head.left_child.add_left_child(Node('D'))
		self.binary_tree.head.left_child.add_right_child(Node('E'))
		#          'A'
		#         /  \
		#      'B'   'C'
		#     /  \
		#  'D'   'E'
	# END setUp


	# def test_init(self):

	# END test_init

	def test_contains(self):
		 # test for head
		self.assertTrue(self.binary_tree.contains(Node('A')))
		# test for child
		self.assertTrue(self.binary_tree.contains(Node('D')))
		# test for non-valid
		self.assertFalse(self.binary_tree.contains(Node('F')))
	# END test_contains

	def test_find_LCA(self):
		self.assertEqual(self.binary_tree.find_LCA(Node('D'), Node('C')),
							self.binary_tree.head)
		self.assertEqual(self.binary_tree.find_LCA(Node('D'), Node('E')),
							Node('B'))
	# END test_find_LCA

	def test_find_LCA_invalid(self):
		self.assertFalse(self.binary_tree.find_LCA(Node('B'), Node('F')))
		#with self.assertRaises(exceptions.TypeError):
			#do something
	# END test_find_LCA_invalid

	def test_find_LCA_self(self):
		self.assertEqual(self.binary_tree.find_LCA(Node('B'), Node('D')),
							Node('B'))
	# END test_find_LCA_self

	def test_find_LCA_same(self):
		self.assertEqual(self.binary_tree.find_LCA(Node('C'), Node('C')),
							Node('C'))
	# END test_find_LCA_same
# END TestBinaryTree
