from collections import deque
class Node:
	def __init__(self, key):
		self.key = key
		self.has_edge_to = []
	# END __init__

	def equals(self, node):
		if node is None: return False
		return self.key == node.key
	# END equals

	def add_edge_to(self, node):
		self.has_edge_to.append(node)
	# END __add_edge_to
# END Node

class DirectedGraph:
	def __init__(self):
		self.source = None # Any node that has no edges TO it
		self.nodes = []
		self.edges = {}
	# END __init__

	def equals(self, digraph):
		if digraph is None: return False
		if self.__compare_nodes(digraph.nodes):
			return self.__compare_edges(digraph.edges)
		# END if
		return False
	# END equals

	# TODO
	def __compare_edges(self, cmp_dict):
		for from_self, to_self in self.edges:
			for from_dict in cmp_dict:
				if (not from_self.equals(from_dict)
						and not to_self.equals(cmp_dict[from_dict]):
					continue
				else:
					cmp_dict[from_dict] = None
					break
			# END if
		# END for
		for _, x in cmp_dict:
			if x is not None: return False
		return True
	# END __compare_edges

	def __compare_nodes(self, cmp_list):
		if cmp_list is None: return False
		if len(cmp_list)!=len(self.nodes): return False
		for n in self.nodes:
			for i in range(0, len(cmp_list)):
				if not n.equals(cmp_list[i]): continue
				else:
					cmp_list[i] = None
					break
				# END if/else
			# END inner for
		# END outer for
		for x in list:
			if x is not None: return False
		# END for
		return True


	def add_node(self, node):
		if node is not None:
			self.nodes.append(node)
		# END if
	# END add_node

	def add_edge_key(self, from_key, to_key):
		self.add_edge(Node(from_key), Node(to_key))

	def add_edge(self, from_node, to_node):
		if to_node is None or from_node is None: return
		if self.contains(to_node) and self.contains(from_node):
			self.edges[from_node] = to_node
			from_node.add_edge_to(to_node)
			if self.source is None or self.source.equals(to_node):
				self.set_source
			# END if
		# END if
	# END add_edge

	def set_source(self):
		for x in self.nodes:
			source_found = True
			for from_node, to_node in self.edges:
				if to_node.equals(x): source_found = False
			if source_found:
				self.source = x
				return
		# END for
		# if no new source found, graph is cyclic
		raise ValueError('Graph has no source, graph is cyclic.')

	def contains(self, goal_node):
		# checks if node with passed key is in the tree, returns boolean
		# returns True if None is passed when nodes list is empty
		if goal_node is None:
			return len(self.nodes)==0
		for x in self.nodes:
			if x.equals(goal_node): return True
		# END for
		return False
	# END contains

	def find_LCA(self, p, q):
		if not self.contains(p) or not self.contains(q):
			return None
		path_p = self.shortest_path(p)
		path_q = self.shortest_path(q)
		for i in range(1,len(path_p)):
			if not path_p[i].equals(path_q[i]):
				return path_p[i-1]
	# END find_LCA

	# based on code from
	# https://gist.github.com/mdsrosa/c71339cb23bc51e711d8
	def shortest_path(self, dest):
		paths = self.generate_paths()
		path = [self.source]
		_dest = paths[dest] # TODO fix indexing
		while not _dest.equals(self.source):
			path.append(_dest)
			_dest = paths[_dest] # TODO fix indexing
		# END while
		path.append(dest)
		return path
	# END shortest_path

	# based on dijkstra's algorithm in python
	# https://gist.github.com/econchick/4666413
	def generate_paths(self):
		visited = {self.source: 0}
		paths = {}
		tmp_nodes = set(self.nodes)

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
			if min_node is None: break

			tmp_nodes.remove(min_node)
			for edge in min_node.has_edge_to:
				if edge not in visited:
					paths[edge] = min_node
				# END if
			# END for
		# END while
		return paths
	# END generate_paths
# END BinaryTree
