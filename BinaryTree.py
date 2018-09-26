
class Node:
    def ___init___(self, key):
        self.key = key
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
# END Node

class BinaryTree:

    def ___init___(self, head):
        self.head = head
    # END ___init___

    def contains(self, key):
        # checks if node with passed key is in the tree, returns boolean
        return containsR(key, self.head)
    # END contains

    def containsR(key, currentNode):
        #recursively finds the node with the passed key
        if currentNode == None: return None
        if key == currentNode.key: return currentNode

        if currentNode.is_parent:
            node = containsR(key, currentNode.left_child)
            if node == None: node = containsR(key, currentNode.right_child)
            return node
        # END if
        return None
    # END containsR

    def find_LCA(self, node1, node2):
        # finds the LCA of the 2 nodes passed, returns node that is LCA
        b1 = self.contains(node1.key)
        b2 = self.contains(node2.key)
    # END find_LCA
# END BinaryTree
