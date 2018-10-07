
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

class BinaryTree:
	def __init__(self, head):
		self.source = head
		self.nodes = []
		self.edges = {}
	# END __init__

	def equals(self, tree):
		if tree is None: return False
		return self.__compare_nodes(self.source, tree.source)
	# END equals

	def __compare_nodes(self, p, q):
		# recursively compares node1 in the tree with node2 from another tree
		if p is None and q is None: return True
		if (p.equals(q) and
				node1.is_parent == node2.is_parent and
				self.__compare_nodes(node1.left_child, node2.left_child) and
				self.__compare_nodes(node1.right_child, node2.right_child)):
			return True
		# END if
		return False
	# END __compare_nodes

	def add_node(self, node):
		if none is not None:
			self.nodes.append(node)
		# END if
	# END add_node

	def add_edge(self, to, from):
		if edge is None: return
		if self.contains(to) and self.contains(from):
			self.edges[from] = to
			from.__add_edge_to(to)
		# END if
	# END add_edge

	def contains(self, goal_node):
		# checks if node with passed key is in the tree, returns boolean
		return self.__contains_rec(goal_node, self.source)
	# END contains

	def __contains_rec(self, goal_node, currentNode):
		#recursively finds the node with the passed key
		if currentNode is None: return None
		if goal_node.equals(currentNode): return currentNode

		if len(currentNode.edges_from)>0:
			found_node = self.__contains_rec(goal_node, currentNode.left_child)
			if found_node is None:
				found_node = self.__contains_rec(
								goal_node, currentNode.right_child)
			# END if
			return found_node
		# END if
		return None
	# END __contains_rec

	def __contains_rec(self, current, goal, path=[]):
		path = path + [start]
		if current.equals(goal):
			return path
		for node in self.nodes:
			if node not in path:
				newpath = find_path(graph, node, end, path)
				if newpath: return newpath
		# END for
		return None
	# END __contains_rec

	def find_LCA(self, p, q):
		p_found = self.contains(p)
		q_found = self.contains(q)
		if p_found is None or q_found is None:
			return None
		return self.__find_LCA(self.head, p, q)
	# END find_LCA

	# code adapted from https://stackoverflow.com/a/46454780
	def __find_LCA(self, root, p, q):
		# finds the LCA of the 2 nodes passed, returns node that is LCA
		if root is None: return None
		flag=0
		if p.key == root.key or q.key == root.key:
			flag=1
			#indicates later to return root
		# END if

		left = self.__find_LCA(root.left_child, p, q)
		right = self.__find_LCA(root.right_child, p, q)

		if left is None and right is None:
			if flag==0: return None
			# else flag == 1
			return root

		if left is not None and right is not None:
			return root

		if left is None:
			if flag==1:
				if ((not right.equals(p) and not right.equals(q)) or
						right.equals(root)):
					return right
				if not right.equals(root):
					return root
			# else flag != 1
			return right

		# else right is None:
		if flag==1:
			if ((not left.equals(p) and not left.equals(q)) or
					left.equals(root)):
				return left
			if not left.equals(root):
				return root
		# else flag != 1
		return left
	# END __find_LCA

	# based on dijkstra's algorithm in python
	# https://gist.github.com/econchick/4666413
	def __contains_rec(self, goal_node):
		visited = {self.source: 0}
		path = {}

		while nodes:
			min_node = None
			for node in nodes:
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
		nodes.remove(min_node)
		current_weight = visited[min_node]

		for edge in graph.edges[min_node]:
			weight = current_weight + graph.distance[(min_node, edge)]
			if edge not in visited or weight < visited[edge]:
				visited[edge] = weight
				path[edge] = min_node
			# END if
		# END for
	return visited, path
	# ENd LCA_dijsktra
# END BinaryTree
