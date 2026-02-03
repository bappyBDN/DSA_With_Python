"""Given a binary tree, the task is to check for every node,
 its value is equal to the sum of values of its immediate left and right child. 
 For NULL values, consider the value to be 0.
 Also, leaves are considered to follow the property."""

from logging import root


class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
def isChildrenSumProperty(node):
    if node is None or (node.left is None and node.right is None):
        return 1
    SUM=0
    
    if node.left is not None:
        SUM += node.left.data
    if node.right is not None:
        SUM += node.right.data
    return True if (node.data ==SUM and
                 isChildrenSumProperty(node.left) and
                 isChildrenSumProperty(node.right)) else False
# Example usage:
# Constructing a binary tree
#         10
#        /  \
#       8    2
root = Node(10)
root.left = Node(8)
root.right = Node(2)
if isChildrenSumProperty(root):
    print("The tree follows the Children Sum Property")
else:
    print("The tree does not follow the Children Sum Property")

