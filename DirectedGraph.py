
class Node:
	def __init__(self, key):
		self.key = key
		self.has_edge_to = []
	# END __init__

	def equals(self, node):
		if node is None: return False
		return self.key == node.key
	# END equals

	def __add_edge_to(self, node):
		self.has_edge_to.append(node)
	# END __add_edge_from
# END Node

class DirectedGraph:
	def __init__(self):
		self.source = None # Any node that has no edges TO it
		self.nodes = []
		self.edges = {}
	# END __init__

	def equals(self, digraph):
		if digraph is None: return False
		if set(self.nodes) == set(digraph.nodes):
			return self.__compareEdges(digraph)
		# END if
		return False
	# END equals

	# TODO
	def __compareEdges(self, digraph):
		return False

	def add_node(self, node):
		if none is not None:
			self.nodes.append(node)
		# END if
	# END add_node

	def add_edge_key(self, to_key, from_key):
		self.add_edge(Node(to_key), Node(from_key))

	def add_edge(self, to, from):
		if to is None or from is None: return
		if self.contains(to) and self.contains(from):
			self.edges[from] = to
			from.__add_edge_to(to)
			if self.source is None or self.source.equals(to):
				self.set_source
			# END if
		# END if
	# END add_edge

	def set_source(self):
		for x in self.nodes:
			source_found = True
			for from,to in self.edges:
				if to.equals(x): source_found = False
			if source_found:
				self.source = x
				return
		# END for
		# if no new source found, graph is cyclic
		raise ValueError('Graph has no source, graph is cyclic.')

	def contains(self, goal_node):
		# checks if node with passed key is in the tree, returns boolean
		for x in self.nodes:
			if x.equals(goal_node): return x
		# END for
		return None
	# END contains

	def find_LCA(self, p, q):
		p_found = self.contains(p)
		q_found = self.contains(q)
		if p_found is None or q_found is None:
			return None
		path_p = self.shortest_path(p)
		path_q = self.shortest_path(q)
		for i in range(0,len(path_p)):
			if !path_p[i].equals(path_q[i]):
				return path_p[i-1]
	# END find_LCA

	# based on code from
	# https://gist.github.com/mdsrosa/c71339cb23bc51e711d8
	def shortest_path(self, dest):
		paths = self.generate_paths()
		path = []
		path.append(self.source)
		_dest = paths[dest]
		while !dest_p.equals(self.source):
			path.append(_dest)
			_dest = paths[_dest]
		# END while
		path.append(dest)
		return path
	# END shortest_path

	# based on dijkstra's algorithm in python
	# https://gist.github.com/econchick/4666413
	def generate_paths(self):
		visited = {self.source: 0}
		paths = {}
		tmp_nodes = self.nodes

		while tmp_nodes:
			min_node = None
			for node in tmp_nodes:
				if node in visited:
					if min_node is None:
						min_node = node
					elif visited[node] < visited[min_node]:
						min_node = node
					# END if
			# END for
		# END while
		if min_node is None:
			break
		# END if
		tmp_nodes.remove(min_node)
		for edge in graph.edges[min_node]:
			if edge not in visited:
				paths[edge] = min_node
			# END if
		# END for
	return paths
	# END generate_paths
# END BinaryTree
