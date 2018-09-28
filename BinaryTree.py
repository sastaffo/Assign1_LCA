
class Node:
	def __init__(self, key):
		self.key = key
		self.is_parent = False
		self.left_child = None
		self.right_child = None
	# END __init__

	def equals(self, node):
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

	# code adapted from https://stackoverflow.com/a/46454780
	def find_LCA(self, root, p, q):
		# finds the LCA of the 2 nodes passed, returns node that is LCA
		flag=0
		if root is None: return None
		if p.key == root.key or q.key == root.key:
			flag=1
			#return root

		left_subtree = self.find_LCA(root.left_child, p, q)
		right_subtree = self.find_LCA(root.right_child, p, q)

		if left_subtree is None and right_subtree is None:
			if flag==0: return None
			return root

		if left_subtree is not None and right_subtree is not None:
			return root

		if left_subtree is None:
			if flag==1:
				if ((right_subtree.value!=p and right_subtree.value!=q) or
						right_subtree.value==root.value):
					return right_subtree
				if right_subtree.value!=root.value:
					return root
				return right_subtree
		# else right_subtree is None
		if flag==1:
			if ((left_subtree.key!=p and left_subtree.value!=q) or
					left_subtree.key==root.key):
				return left_subtree
			if left_subtree.value!=root.value:
				return root
		# else flag != 1
		return left_subtree
	# END find_LCA
# END BinaryTree
