from collections import deque
class Node:
	def __init__(self, key):
		self.key = key
		self.has_edge_to = [] # list of KEYS
	# END __init__

	def equals(self, node):
		if node is None: return False
		return self.key == node.key
	# END equals

	def add_edge_to(self, key):
		if key is not None:
			for x in self.has_edge_to:
				if x==key: return
			self.has_edge_to.append(key)
	# END __add_edge_to
# END Node

class DirectedGraph:
	def __init__(self):
		self.source = None # Any node that has no edges TO it
		self.nodes = [] # list of nodes
		self.edges = {} # dictionary of KEYS of nodes = from_key:to_key
	# END __init__

	def equals(self, digraph):
		if digraph is None: return False
		if self.compare_nodes(digraph.nodes):
			return self.compare_edges(digraph.edges)
		# END if
		return False
	# END equals


	def compare_edges(self, cmp_dict):
		if cmp_dict is None: return False
		if len(cmp_dict)!=len(self.edges): return False
		for from_self, to_self in self.edges:
			for from_dict in cmp_dict:
				if (not from_self==from_dict
						and not to_self==cmp_dict[from_dict]):
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

	def compare_nodes(self, cmp_list):
		if cmp_list is None: return False
		if len(cmp_list)!=len(self.nodes): return False
		for n in self.nodes:
			for i in range(len(cmp_list)):
				if not n.equals(cmp_list[i]): continue
				else:
					cmp_list[i] = None
					break
				# END if/else
			# END inner for
		# END outer for
		for x in cmp_list:
			if x is not None: return False
		# END for
		return True


	def add_node(self, node):
		if node is not None:
			for x in self.nodes:
				if x.equals(node): return
			self.nodes.append(node)
		# END if
	# END add_node

	def add_edge(self, from_key, to_key):
		if from_key is None or to_key is None: return
		from_node = self.contains(Node(from_key))
		to_node = self.contains(Node(to_key))
		if from_node is not None and to_node is not None:
			for from_exists, to_exists in self.edges.items():
				if (from_exists==from_key and to_exists==to_key):
					return
			self.edges.update({from_key:to_key})
			from_node.add_edge_to(to_key)
			if self.source is None or self.source.equals(to_node):
				self.set_source()
			# END if
		# END if
	# END add_edge

	def add_edge_node(self, from_node, to_node):
		self.add_edge(from_node.key, to_node.key)
	# END add_edge_node

	def set_source(self):
		for x in self.nodes:
			source_found = True
			for from_key, to_key in self.edges.items():
				if x.key==to_key: source_found = False
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
			if x.equals(goal_node): return goal_node
		# END for
		return None
	# END contains

	def find_LCA(self, p, q):
		if self.contains(p) is None or self.contains(q) is None:
			return None
		path_p = self.shortest_path(p)
		path_q = self.shortest_path(q)
		for i in range(len(path_p)):
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
		if self.source is None: self.set_source()
		visited = [self.source.key]
		paths = {}
		tmp_nodes = set(self.nodes)

		while tmp_nodes:
			min_node = None
			for node in tmp_nodes:
				if node.key in visited:
					if min_node is None:
						min_node = node
					# END if
			# END for
			if min_node is None: break

			tmp_nodes.remove(min_node)
			for dest_key in min_node.has_edge_to:
				if dest_key not in visited:
					paths[dest_key] = min_node.key
				# END if
			# END for
		# END while
		return paths
	# END generate_paths
# END BinaryTree
