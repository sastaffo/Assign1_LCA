from collections import deque

class DirectedGraph:
	def __init__(self):
		self.source = None # Any node that has no edges TO it
		self.nodes = [] # list of nodes
		self.edges = {} # dictionary of KEYS of nodes = _from:[_to,_to]
	# END __init__

	def equals(self, digraph):
		if digraph is not None:
			if set(self.nodes)==set(digraph.nodes):
				return self.compare_edges(digraph.edges)
		# END if
		return False
	# END equals


	def compare_edges(self, cmp_dict):
		if cmp_dict is None: return False
		if len(cmp_dict)!=len(self.edges): return False
		for from_self, to_list in self.edges.items():
			for from_dict in cmp_dict:
				for to_self in to_list:
					if not from_self==from_dict:
						continue
					else:
						break
			# END if
		# END for
		for _, x in cmp_dict.items():
			if x is not None: return False
		return True
	# END __compare_edges

	def add_node(self, node):
		if node is not None:
			if node not in self.nodes:
				self.nodes.append(node)
		# END if
	# END add_node

	def add_edge(self, _from, _to):
		if _from is None or _to is None: return
		bool_from, _ = self.contains(_from)
		bool_to, _ = self.contains(_to)
		if bool_from and bool_to:
			if _from in self.edges:
				self.edges[_from].append(_to)
			else:
				self.edges.update({_from:[_to]})
			# END if
			if self.source is None or self.source==_to:
				self.set_source()
			# END if
		# END if
	# END add_edge

	def set_source(self):
		for x in self.nodes:
			source_found = True
			for _from, _to in self.edges.items():
				if x==_to: source_found = False
			if source_found:
				self.source = x
				return
		# END for
		# if no new source found, graph is cyclic
		raise ValueError('Graph has no source, graph is cyclic.')

	def contains(self, goal):
		# checks if node with passed key is in the tree, returns boolean
		# returns True if None is passed when nodes list is empty
		if goal is None: return (len(self.nodes)==0),None
		if goal in self.nodes: return True,goal
		return False,None
	# END contains

	def find_LCA(self, p, q):
		if self.contains(p) is None or self.contains(q) is None:
			return None
		path_p = self.shortest_path(p)
		path_q = self.shortest_path(q)
		for i in range(len(path_p)):
			if not path_p[i]==path_q[i]:
				return path_p[i-1]
	# END find_LCA

	# based on code from
	# https://gist.github.com/mdsrosa/c71339cb23bc51e711d8
	def shortest_path(self, dest):
		print(self.nodes)
		print(self.edges)
		if self.source is not None: print(self.source)
		else: print("no source")
		paths = self.generate_paths()
		print(self.source)
		path = [self.source]
		print("dest:" + dest)
		print(paths)
		_dest = paths[dest] # TODO fix indexing
		while not _dest==self.source:
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
		visited = {self.source:0} # let all edges have a weight of 1

		weights = []
		for _from,_to in self.edges.items():
			weights.append([_from,_to,1])
		paths = {}
		tmp_nodes = set(self.nodes)

	#	weights = {}
	#	for _from,_to in self.edges.items():
	#		weights.update({(_from,_to):1})
	#	paths = {}
	#	tmp_nodes = set(self.nodes)

		while tmp_nodes:
			min_node = None
			for node in tmp_nodes:
				if node in visited:
					if (min_node is None or
							visited[node] < visited[min_node]):
						min_node = node
					# END if
				# END if
			# END for
			if min_node is None: break

			tmp_nodes.remove(min_node)
			curr_weight = visited[min_node]
			min_node_list = self.edges.get(min_node)
			if min_node_list is not None:
				for dest_key in min_node_list:
					try:
						weight = curr_weight + 1
					except: continue
					# END try
					if dest_key not in visited or weight < visited[dest_key]:
						visited[dest_key] = weight
						paths.update({dest_key:min_node})
					# END if
				# END for
		# END while
		return paths
	# END generate_paths
# END BinaryTree
