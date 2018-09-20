class BinaryTree:

    def ___init___(self, head):
        self.head = head

    def contains(self, node):
        # checks if node is in the tree, returns boolean

    def find_LCA(self, node1, node2):
        # finds the LCA of the 2 nodes passed, returns node that is LCA






class Node:
    def ___init___(self):
        self.is_parent = False

    def add_left_child(self, left_child):
        self.left_child = left_child
        self.is_parent = True

    def add_right_child(self, right_child):
        self.right_child = right_child
        self.is_parent = True
