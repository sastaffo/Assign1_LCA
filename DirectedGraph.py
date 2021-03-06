from collections import deque
DEBUG = True
class DirectedGraph:
	def __init__(self):
		self.source = None # Any node that has no edges TO it
		self.nodes = [] # list of nodes
		self.edges = [] # list of tuples [(_from, _to)]
	# END __init__

	def equals(self, digraph):
		if digraph is not None:
			if set(self.nodes)==set(digraph.nodes):
				return self.compare_edges(digraph.edges)
		# END if
		return False
	# END equals

	def compare_edges(self, other_edges):
		if other_edges is None: return False
		if len(other_edges)!=len(self.edges): return False
		for self_tuple in self.edges:
			for i in range(len(other_edges)):
				if tuple_equals(self_tuple, other_edges[i]):
					other_edges[i] = (None,None)
					break
				# END if
			# END for
		# END for
		for tuple in other_edges:
			if not tuple_equals(tuple, (None,None)): return False
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
		if self.contains(_from) and self.contains(_to):
			for self_tuple in self.edges:
				if tuple_equals(self_tuple, (_from,_to)):
					return
				# END if
			# END for
			# edge not present, add edge
			self.edges.append((_from, _to))
			if self.source is None or self.source==_to:
				self.set_source()
			# END if
		# END if
	# END add_edge

	def set_source(self):
		for x in self.nodes:
			source_found = True
			for self_tuple in self.edges:
				if (self_tuple[1]==x): source_found = False
			if source_found:
				self.source = x
				return
		# END for
		# if no new source found, graph is cyclic
		raise ValueError('Graph has no source, graph is cyclic.')

	def contains(self, goal):
		# checks if node with passed key is in the tree, returns boolean
		# returns True if None is passed when nodes list is empty
		if goal is None: return (len(self.nodes)==0)
		if goal in self.nodes: return True
		return False
	# END contains

	def find_LCA(self, p, q):
		if not self.contains(p) or not self.contains(q):
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
		if DEBUG:
			if self.source is not None: print("init source: " + self.source)
			else: print("no source")
		paths = self.generate_paths()
		path = [self.source]
		if DEBUG:
			print("after gen_p source: " + self.source)
			print("dest: " + dest)
			print("paths: ")
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
	# https://gist.github.com/mdsrosa/c71339cb23bc51e711d8
	def generate_paths(self):
		if self.source is None:
			if DEBUG: print("	(gen_p) pre-set source: None")
			self.set_source()
		elif DEBUG: print("	(gen_p) pre-set source: " + self.source)
		if DEBUG:
			print("	(gen_p) post-set source: " + self.source)
		visited = {self.source:0}

		# let all edges have a weight of 1
		weights = {}
		for self_tuple in self.edges:
			weights[self_tuple]=1
		if DEBUG:
			print("	(gen_p) weights: ")
			for x,y in weights.items():
				print("(" + ",".join(x) + "): " + str(y))
		paths = {}
		tmp_nodes = set(self.nodes)
		if DEBUG: print(tmp_nodes)

		while tmp_nodes:
			min_node = None
			for node in tmp_nodes:
				if DEBUG: print("\n\n	(gen_p) current node: '"+ node + "'")
				if node in visited:
					if DEBUG: print("	(gen_p) 	visited:true")
					if (min_node is None or
							visited[node] < visited[min_node]):
						if DEBUG:
							if min_node is not None:
								print("	(gen_p) 	old min: " + min_node)
							print("	(gen_p) 	new min: " + node)
						min_node = node
					# END if
				# END if
			# END for
			if min_node is None: break
			if DEBUG: print("	(gen_p) 	min_node not None")

			tmp_nodes.remove(min_node)
			curr_weight = visited[min_node]
			if DEBUG: print("	(gen_p) 	curr_weight="+ str(curr_weight))
			min_node_list=[]
			# finds nodes where there exists an edge from min_node to that node
			for self_tuple in self.edges:
				if self_tuple[0]==min_node:
					min_node_list.append(self_tuple[1])
			# END for
			if DEBUG:
				print("	(gen_p) 	min_node_list: " + ",".join(min_node_list))
			for _dest in min_node_list:
				try:
					weight = curr_weight + weights[(min_node,dest_key)]
				except:
					continue
				if dest_key not in visited or weight < visited[dest_key]:
					visited[dest_key] = weight
					if DEBUG: print("	(gen_p) 	new weight for node '"
									+ dest_key + "' = " + weight)
					paths.update({dest_key:min_node})
					if DEBUG:
						print("	(gen_p) 	paths: ")
						print(paths)
				# END if
			# END for
		# END while
		return paths
	# END generate_paths
# END BinaryTree

def tuple_equals(tupleA,tupleB):
	if len(tupleA)!=len(tupleB): return False
	for i in range(len(tupleA)):
		if tupleA[i]!=tupleB[i]: return False
	return True
# END tuple_equals
