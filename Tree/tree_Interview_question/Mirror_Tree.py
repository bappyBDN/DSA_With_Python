class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def mirrorTree(root):
    if root is None:
        return 
    # Swap the left and right children
    mirrorTree(root.right)
    mirrorTree(root.left)
    root.left,root.right=root.right,root.left
    return root
    
# Example usage:
# Constructing a binary tree
#         1
#        / \
#       2   3
root = Node(1)
root.left = Node(2)
root.right = Node(3)
mirrored_root = mirrorTree(root)
# The mirrored tree will be:
#         1
#        / \
#       3   2
print(mirrored_root.left.value)  # Output: 3
print(mirrored_root.right.value) # Output: 2
