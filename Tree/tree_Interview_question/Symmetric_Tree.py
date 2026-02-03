"""A tree is Symmetric Tree if is a mirror reflection of itself.
and the value of left subtree is equal to right subtree."""
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
def ismirror(left1,right1):
    if left1 is None and right1 is None:
        return True
    if left1 is None or right1 is None:
        return False
    return (left1.data == right1.data and
            ismirror(left1.left, right1.right) and
            ismirror(left1.right, right1.left))
def isSymmetric(root):
    if root is None:
        return True
    return ismirror(root.left, root.right)
# Example usage:
# Constructing a symmetric binary tree
#         1
#        / \
#       2   2
#      / \ / \
root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(4)
root.right.right = Node(3)
if isSymmetric(root):
    print("The tree is symmetric")
else:
    print("The tree is not symmetric")
    

