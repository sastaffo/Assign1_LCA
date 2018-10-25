
from DirectedGraph import DirectedGraph
import unittest

class TestDirectedGraph(unittest.TestCase):
	def setUp(self):
		# sets up objects to be tested
		self.digraph_building = DirectedGraph()
		# {empty}

		self.digraph = DirectedGraph()
		self.digraph.nodes = ['A', 'B', 'C', 'D', 'E' ]
		self.digraph.edges = {'A':['B','C'], 'B':['D','E'], 'C':['E']}
		#          'A'
		#         /  \
		#      'B'   'C'
		#     /  \  /
		#  'D'   'E'
	# END setUp

	def test_compare_edges(self):
		# edges in correct order
		edgesA = {'A':['B','C'], 'B':['D','E'], 'C':['E']}
		self.assertTrue(self.digraph.compare_edges(edgesA))

		# change one edge
		edgesA['C'][i] = 'A'
		self.assertFalse(self.digraph.compare_edges(edgesA))

		# change one edge to an invalid node
		edgesA['C'][i] = 'X'
		self.assertFalse(self.digraph.compare_edges(edgesA))

		# add an edge so dicts are different size
		edgesA['A'].append('E')
		self.assertFalse(self.digraph.compare_edges(edgesA))

		# edges in a different order: should be true
		edgesB = {'B':['E','D'], 'A':['C','B'], 'C':['E']}
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
		node_list = ['A', 'B']
		# add two nodes
		self.digraph_building.add_node('A')
		self.digraph_building.add_node('B')
		self.assertTrue(set(self.digraph_building.nodes)==set(node_list))

		# add null node
		self.digraph_building.add_node(None)
		self.assertTrue(set(self.digraph_building.nodes)==set(node_list))

		# add existing node
		self.digraph_building.add_node('A')
		self.assertTrue(set(self.digraph_building.nodes)==set(node_list))
	# END test_add_node

	def test_add_edge(self):
		# add new edge
		self.digraph_building.add_node('A')
		self.digraph_building.add_node('B')
		self.digraph_building.add_edge('A','B')
		edges = {'A':['B']}
		self.assertTrue(self.digraph_building.compare_edges(edges))

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


	def test_contains(self):
		# test for none
		b,_ = self.digraph_building.contains(None)
		self.assertTrue(b)
		# test for invalid
		b,_ = self.digraph_building.contains('D')
		self.assertFalse(b)

		# test for None
		b,_ = self.digraph.contains(None)
		self.assertFalse(b)
		# test for valid
		b,_ = self.digraph.contains('A')
		self.assertTrue(b)
		b,_ = self.digraph.contains('D')
		self.assertTrue(b)
		# test for invalid
		b,_ = self.digraph.contains('F')
		self.assertFalse(b)
	# END test_contains

	def test_find_LCA(self):
		self.assertTrue('B'==(self.digraph.find_LCA('D', 'E')))
		self.assertTrue('A'==(self.digraph.find_LCA('B', 'C')))
	# END test_find_LCA

	def test_find_LCA_invalid(self):
		self.assertFalse(self.digraph.find_LCA('B', 'F'))
	# END test_find_LCA_invalid

	def test_find_LCA_self(self):
		self.assertTrue('B'==(self.digraph.find_LCA('B', 'D')))
	# END test_find_LCA_self

	def test_find_LCA_same(self):
		self.assertTrue('C'==(self.digraph.find_LCA('C', 'C')))
	# END test_find_LCA_same

# END TestBinaryTree
