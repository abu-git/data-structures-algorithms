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

#print("root:", node0.key, "left:", node1.key, "right:", node2.key)

node0.left = node1
node0.right = node2

tree = node0
print("root key:", tree.key)
print("left key:", tree.left.key)
print("right key:", tree.right.key)

treeRoot = TreeNode(2)
treeRoot.left = TreeNode(3)
treeRoot.left.left = TreeNode(1)

treeRoot.right = TreeNode(5)
treeRoot.right.left = TreeNode(3)
treeRoot.right.left.right = TreeNode(4)
treeRoot.right.right = TreeNode(7)
treeRoot.right.right.left = TreeNode(6)
treeRoot.right.right.right = TreeNode(8)
print("root:", treeRoot.key)
print("root right:", treeRoot.right.key)
print("root right left:", treeRoot.right.left.key)
print("root right left right:", treeRoot.right.left.right.key)
print("root right right:", treeRoot.right.right.key)
print("root right right left:", treeRoot.right.right.left.key)
print("root right right right:", treeRoot.right.right.right.key)