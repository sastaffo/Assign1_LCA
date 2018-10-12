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

	#def test_add_edge_to(self):
		# TODO write tests here
	# END test_add_edge_to

# END TestNode


class TestDirectedGraph(unittest.TestCase):
	def setUp(self):
		# sets up objects to be tested
		self.digraph_building = DirectedGraph()
		# {empty}

		self.digraph1 = DirectedGraph()
		self.digraph1.nodes = [	Node('A'),  Node('B'),  Node('C'),
								Node('D'),  Node('E') ]
		self.digraph1.edges = {	Node('A') : Node('B'),
								Node('A') : Node('C'),
								Node('B') : Node('D'),
								Node('B') : Node('E'),
								Node('C') : Node('E')}
		#          'A'
		#         /  \
		#      'B'   'C'
		#     /  \  /
		#  'D'   'E'

		self.digraph2 = DirectedGraph()
		self.digraph2.nodes = [	Node('A'), Node('B'), Node('C'), Node('D') ]
		self.digraph2.edges = { Node('A') : Node('B'),
								Node('A') : Node('C'),
								Node('B') : Node('C'),
								Node('C') : Node('D')}
		#     'A'
		#    /  \
		# 'B' -- 'C' -- 'D'
	# END setUp


	def test_equals(self):
		self.assertFalse(self.digraph1.equals(None))
		self.assertFalse(self.digraph1.equals(self.digraph2))
		# TODO add more tests here

		self.assertTrue(self.digraph_building.equals(DirectedGraph()))
		# TODO add more tests here
	# END test_equals


	def test_add_node(self):
		self.assertFalse(self.digraph_building.nodes)
		# add two nodes
		self.digraph_building.add_node(Node('A'))
		self.digraph_building.add_node(Node('B'))
		self.assertEqual(self.digraph_building.nodes, [Node('A'), Node('B')])

		# add null node
		self.digraph_building.add_node(None)
		self.assertEqual(self.digraph_building.nodes, [Node('A'), Node('B')])
	# END test_add_node

	def test_add_edge(self):
		# add new edge
		self.digraph_building.add_node(Node('A'))
		self.digraph_building.add_node(Node('B'))
		self.digraph_building.add_edge(Node('A'),Node('B'))
		self.assertEqual(self.digraph_building.edges, {Node('A'): Node('B')})

		# add existing edge: should not change edge map
		expected_edges = {	Node('A') : Node('B'),
							Node('A') : Node('C'),
							Node('B') : Node('D'),
							Node('B') : Node('E'),
							Node('C') : Node('E')
						 }
		# check equality before making changes
		self.assertEqual(self.digraph1.edges, expected_edges)
		self.digraph1.add_edge(Node('A'), Node('B'))
		self.assertEqual(self.digraph1.edges, expected_edges)

		# add edge to None: should not change edge map
		self.digraph1.add_edge(Node('C'), None)
		self.assertEqual(self.digraph1.edges, expected_edges)

		# add edge to invalid node: should not change edge map
		self.digraph1.add_edge(Node('C'), Node('G'))
		self.assertEqual(self.digraph1.edges, expected_edges)
	# END test_add_edge

	def test_add_edge_key(self):
		self.digraph_building.add_node(Node('A'))
		self.digraph_building.add_node(Node('B'))
		self.digraph_building.add_edge_key('A','B')
		self.assertEqual(self.digraph_building.edges, {Node('A'): Node('B')})
		self.digraph_building.add_node(Node('B'))

	def test_contains(self):
		 # test for source
		self.assertTrue(self.digraph_building.contains(Node('A')))
		# test for non-valid
		self.assertFalse(self.digraph_building.contains(Node('D')))

		# test for source
		self.assertTrue(self.digraph1.contains(Node('A')))


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
