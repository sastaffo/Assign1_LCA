
class Node:
	def __init__(self, key):
		self.key = key
		self.is_parent = False
		self.left_child = None
		self.right_child = None
	# END __init__

	def equals(self, node):
		if node == None: return False
		if self.key == node.key:
			return True
		return False
	# END equals

	def add_left_child(self, left_child):
		self.left_child = left_child
		self.is_parent = True
	# END add_left_child

	def add_right_child(self, right_child):
		self.right_child = right_child
		self.is_parent = True
	# END add_right_child
# END Node

class BinaryTree:

	def __init__(self, head):
		self.head = head
	# END __init__

	def equals(self, tree):
		return self.head.__compare_nodes(tree.head)
	# END equals

	def __compare_nodes(self, node1, node2):
		# recursively compares node1 in the tree with node2 from another tree
		if node1 == None and node2 == None: return True
		if (node1.key.equals(node2.key) and
				node1.is_parent == node2.is_parent and
				self.__compare_nodes(node1.left_child, node2.left_child) and
				self.__compare_nodes(node1.right_child, node2.right_child)):
			return True
		# END if
		return False
	# END __compare_nodes

	def contains(self, node):
		# checks if node with passed key is in the tree, returns boolean
		return self.__contains_rec(node, self.head)
	# END contains

	def __contains_rec(self, node, currentNode):
		#recursively finds the node with the passed key
		if currentNode == None: return None
		if node.key == currentNode.key: return currentNode

		if currentNode.is_parent:
			node_tmp = self.__contains_rec(node.key, currentNode.left_child)
			if node_tmp == None: node_tmp = self.__contains_rec(node.key, currentNode.right_child)
			return node_tmp
		# END if
		return None
	# END __contains_rec

	def find_LCA(self, p, q):
		self.__find_LCA(self.head, p, q)
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
# END BinaryTree
