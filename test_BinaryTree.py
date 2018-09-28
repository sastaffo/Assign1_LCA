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
		self.assertFalse(self.node.equals(None))
		self.assertTrue(self.node.equals(Node('A')))
		self.assertFalse(self.node.equals(Node('E')))

	def test_is_parent(self):
		self.assertFalse(self.node.is_parent)
		self.node.add_left_child(None)
		# node should not be a parent if a None child is added
		self.assertFalse(self.node.is_parent)

		self.node.add_left_child(Node('B'))
		self.assertTrue(self.node.is_parent)

		self.node.add_left_child(None)
		# node should not be parent is child has been replaced with None
		self.assertFalse(self.node.is_parent)

		self.node.add_left_child(Node('B'))
		self.node.add_right_child(Node('C'))
		self.assertTrue(self.node.is_parent)

		self.node.add_left_child(None)
		# node should still be parent if only one child is replaced with None
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


	def test_equals(self):
		self.assertFalse(self.binary_tree.equals(None))
		tree = BinaryTree(Node('A'))
		tree.head.add_left_child(Node('B'))
		# contains some but not all nodes found in self.binary_tree
		self.assertFalse(self.binary_tree.equals(tree))

		tree.head.add_right_child(Node('C'))
		tree.head.left_child.add_left_child(Node('D'))
		tree.head.left_child.add_right_child(Node('E'))
		# contains all notes from self.binary_tree in the right order
		self.assertTrue(self.binary_tree.equals(tree))

		tree.head.right_child.add_left_child(Node('F'))
		# contains all nodes from self.binary_tree and one other
		self.assertFalse(self.binary_tree.equals(tree))

		tree = BinaryTree(Node('A'))
		tree.head.add_left_child(Node('C'))
		tree.head.add_right_child(Node('B'))
		tree.head.left_child.add_left_child(Node('D'))
		tree.head.left_child.add_right_child(Node('E'))
		# contains all nodes from self.binary_tree in the wrong order
		self.assertFalse(self.binary_tree.equals(tree))
	# END test_equals

	def test_contains(self):
		 # test for head
		self.assertTrue(self.binary_tree.contains(Node('A')))
		# test for child
		self.assertTrue(self.binary_tree.contains(Node('D')))
		# test for non-valid
		self.assertFalse(self.binary_tree.contains(Node('F')))
	# END test_contains

	def test_find_LCA(self):
		self.assertTrue(self.binary_tree.head.equals(
				self.binary_tree.find_LCA(Node('D'), Node('C'))))
		self.assertTrue(Node('B').equals(
				self.binary_tree.find_LCA(Node('D'), Node('E'))))
	# END test_find_LCA

	def test_find_LCA_invalid(self):
		self.assertFalse(self.binary_tree.find_LCA(Node('B'), Node('F')))
		#with self.assertRaises(exceptions.TypeError):
			#do something
	# END test_find_LCA_invalid

	def test_find_LCA_self(self):
		self.assertTrue(Node('B').equals(
				self.binary_tree.find_LCA(Node('B'), Node('D'))))
	# END test_find_LCA_self

	def test_find_LCA_same(self):
		self.assertTrue(Node('C').equals(
				self.binary_tree.find_LCA(Node('C'), Node('C'))))
	# END test_find_LCA_same
# END TestBinaryTree
