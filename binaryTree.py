'''
    Implement a binary tree using Python, and show its usage with some examples.


    To begin, we'll create simple binary tree (without any of the additional properties) containing numbers as keys within the nodes.

'''


class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


#   Let's create objects to represent a node of a tree
node0 = TreeNode(3)
node1 = TreeNode(4)
node2 = TreeNode(5)

print("root:", node0.key, "left:", node1.key, "right:", node2.key)

node0.left = node1
node0.right = node2