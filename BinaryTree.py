
class Node:
	def __init__(self, key):
		self.key = key
		self.is_parent = False
		self.left_child = None
		self.right_child = None
	# END __init__

	def equals(self, node):
		if node is None: return False
		if self.key == node.key:
			return True
		return False
	# END equals

	def add_left_child(self, left_child):
		# if null is passed, child is deleted
		self.left_child = left_child
		if left_child is not None: self.is_parent = True
		# if node has no other child and left_child is now null
		elif self.right_child is None: self.is_parent = False
	# END add_left_child

	def add_right_child(self, right_child):
		# if null is passed, child is deleted
		self.right_child = right_child
		if right_child is not None: self.is_parent = True
		# if node has no other child and right_child is now null
		elif self.left_child is None: self.is_parent = False
	# END add_right_child
# END Node

class BinaryTree:

	def __init__(self, head):
		self.head = head
	# END __init__

	def equals(self, tree):
		if tree is None: return False
		return self.__compare_nodes(self.head, tree.head)
	# END equals

	def __compare_nodes(self, node1, node2):
		# recursively compares node1 in the tree with node2 from another tree
		if node1 is None and node2 is None: return True
		if (node1.equals(node2) and
				node1.is_parent == node2.is_parent and
				self.__compare_nodes(node1.left_child, node2.left_child) and
				self.__compare_nodes(node1.right_child, node2.right_child)):
			return True
		# END if
		return False
	# END __compare_nodes

	def contains(self, goal_node):
		# checks if node with passed key is in the tree, returns boolean
		return self.__contains_rec(goal_node, self.head)
	# END contains

	def __contains_rec(self, goal_node, currentNode):
		#recursively finds the node with the passed key
		if currentNode is None: return None
		if goal_node.equals(currentNode): return currentNode

		if currentNode.is_parent:
			found_node = self.__contains_rec(goal_node, currentNode.left_child)
			if found_node is None:
				found_node = self.__contains_rec(
								goal_node, currentNode.right_child)
			# END if
			return found_node
		# END if
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
# END BinaryTree
