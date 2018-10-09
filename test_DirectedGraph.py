#
#

from DirectedGraph import DirectedGraph
from DirectedGraph import Node
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

	def test_add_edge_to(self):
		self.assertEqual()
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


class TestDirectedGraph(unittest.TestCase):
	def setUp(self):
		# sets up object to be tested
		self.digraph = DirectedGraph(Node('A'))
		#          'A'
		#         /  \
		#      'B'   'C'
		#     /  \  /
		#  'D'   'E'
	# END setUp


	def test_equals(self):
		self.assertFalse(self.digraph.equals(None))
		# ADD more tests here
	# END test_equals

	def test_add_node(self):
		self.digraph.add_node(Node('B'))
		self.assertEqual(self.digraph.nodes, [Node('A'), Node('B')])
		self.digraph.add_node(None)
		self.assertEqual(self.digraph.nodes, [Node('A'), Node('B')])
	# END test_add_node

	def test_add_edge(self):
		self.digraph.add_node(Node('B'))
		self.digraph.add_edge(Node('A'),Node('B'))
		self.assertEqual(self.digraph.edges, {Node('A'): Node('B')})
	# END test_add_edge

	def test_add_edge_key(self):
		self.digraph.add_node(Node('B'))
		self.digraph.add_edge_key('A','B')
		self.assertEqual(self.digraph.edges, {Node('A'): Node('B')})

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
