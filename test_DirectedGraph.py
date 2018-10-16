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

		self.digraph = DirectedGraph()
		self.digraph.nodes = [	Node('A'),  Node('B'),  Node('C'),
								Node('D'),  Node('E') ]
		self.digraph.edges = {	'A':'B', 'A':'C',
								'B':'D', 'B':'E',
								'C':'E'}
		#          'A'
		#         /  \
		#      'B'   'C'
		#     /  \  /
		#  'D'   'E'
	# END setUp

	def test_compare_nodes(self):
		# nodes in correct order
		nodesA = [Node('A'), Node('B'), Node('C'), Node('D'), Node('E')]
		self.assertTrue(self.digraph.compare_nodes(nodesA))

		# change one node in list to duplicate existing node
		nodesA[2] = Node('D')
		self.assertFalse(self.digraph.compare_nodes(nodesA))

		# add a node so lists have different lengths
		nodesA[5] = Node('F')
		self.assertFalse(self.digraph.compare_nodes(nodesA))

		# nodes in different order: should be true
		nodesB = [Node('B'), Node('E'), Node('A'), Node('D'), Node('C')]
		self.assertTrue(self.digraph.compare_nodes(nodesB))
	# END test_compare_nodes

	def test_compare_edges(self):
		# edges in correct order
		edgesA = {'A':'B', 'A':'C', 'B':'D', 'B':'E', 'C':'E'}
		self.assertTrue(self.digraph.compare_edges(edgesA))

		# change one edge
		edgesA['C'] = 'A'
		self.assertFalse(self.digraph.compare_edges(edgesA))

		# add an edge so dicts are different size
		edgesA.update({'A':'E'})
		self.assertFalse(self.digraph.compare_edges(edgesA))

		# edges in a different order: should be true
		edgesB = {'A':'C', 'B':'E', 'A':'B', 'C':'E', 'B': 'D'}
		self.assertTrue(self.digraph.compare_edges(edgesB))
	# END test_compare_edges


	def test_equals(self):
		self.assertFalse(self.digraph.equals(None))
		self.assertFalse(self.digraph.equals(self.digraph_building))
		# TODO add more tests here

		self.assertTrue(self.digraph_building.equals(DirectedGraph()))
		# TODO add more tests here
	# END test_equals


	def test_add_node(self):
		self.assertFalse(self.digraph_building.nodes)
		# add two nodes
		self.digraph_building.add_node(Node('A'))
		self.digraph_building.add_node(Node('B'))
		self.assertTrue(self.digraph_building.compare_nodes(
						[Node('A'), Node('B')]))

		# add null node
		self.digraph_building.add_node(None)
		self.assertTrue(self.digraph_building.compare_nodes(
						[Node('A'), Node('B')]))
	# END test_add_node

	def test_add_edge(self):
		# add new edge
		self.digraph_building.add_node(Node('A'))
		self.digraph_building.add_node(Node('B'))
		self.digraph_building.add_edge('A','B')
		self.assertTrue(self.digraph_building.compare_edges({'A':'B'}))

		# add existing edge: should not change edge map
		expected_edges = self.digraph.edges
		# check equality before making changes
		self.digraph.add_edge('A','B')
		self.assertTrue(self.digraph.compare_edges(expected_edges))

		# add edge to None: should not change edge map
		self.digraph.add_edge('C', None)
		self.assertTrue(self.digraph.compare_edges(expected_edges))

		# add edge to invalid node: should not change edge map
		self.digraph.add_edge('C','G')
		self.assertTrue(self.digraph.compare_edges(expected_edges))

		# add edge from node to itself: not valid, should not change edge map
		self.digraph.add_edge('D','D')
		self.assertTrue(self.digraph.compare_edges(expected_edges))
	# END test_add_edge

	def test_add_edge_node(self):
		self.digraph_building.add_node(Node('A'))
		self.digraph_building.add_node(Node('B'))
		self.digraph_building.add_edge_node(Node('A'),Node('B'))
		self.assertTrue(self.digraph_building.compare_edges({'A':'B'}))

	def test_contains(self):
		# test for none
		self.assertTrue(self.digraph_building.contains(None))
		# test for invalid
		self.assertFalse(self.digraph_building.contains(Node('D')))

		# test for None
		self.assertFalse(self.digraph.contains(None))
		# test for valid
		self.assertTrue(self.digraph.contains(Node('A')))
		self.assertTrue(self.digraph.contains(Node('D')))
		# test for invalid
		self.assertFalse(self.digraph.contains(Node('F')))
	# END test_contains

	def test_find_LCA(self):
		self.assertTrue(Node('B').equals(
				self.digraph.find_LCA(Node('D'), Node('E'))))
		self.assertTrue(Node('A').equals(
				self.digraph.find_LCA(Node('B')), Node('C')))
	# END test_find_LCA

	def test_find_LCA_invalid(self):
		self.assertFalse(self.digraph.find_LCA(Node('B'), Node('F')))
	# END test_find_LCA_invalid

	def test_find_LCA_self(self):
		self.assertTrue(Node('B').equals(
				self.digraph.find_LCA(Node('B'), Node('D'))))
	# END test_find_LCA_self

	def test_find_LCA_same(self):
		self.assertTrue(Node('C').equals(
				self.digraph.find_LCA(Node('C'), Node('C'))))
	# END test_find_LCA_same

# END TestBinaryTree
