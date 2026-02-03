class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def maxDepth(root):
    if root is None:
        return 0
    else:
        left_depth = maxDepth(root.left)
        right_depth = maxDepth(root.right)
        return max(left_depth, right_depth) + 1
# Example usage:
# Constructing a binary tree
#         1
#        / \
#       2   3
#      / \   \
#     4   5   6
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)
print(maxDepth(root))  # Output: 3