class BinaryTree:

    def ___init___(self, head):
        self.head = head
	# END ___init___

    def contains(self, node):
        # checks if node is in the tree, returns boolean
	# END contains

    def find_LCA(self, node1, node2):
        # finds the LCA of the 2 nodes passed, returns node that is LCA
	# END find_LCA






class Node:
    def ___init___(self, value):
		self.value = value
        self.is_parent = False
	# END ___init___

    def add_left_child(self, left_child):
        self.left_child = left_child
        self.is_parent = True
	# END add_left_child

    def add_right_child(self, right_child):
        self.right_child = right_child
        self.is_parent = True
	# END add_right_child