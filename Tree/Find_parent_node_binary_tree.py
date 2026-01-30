
class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
def findParentNode(root:Node, target):
    if root is None:
        return None
    if (root.left is not None and root.left.val == target) or (root.right is not None and root.right.val == target):
        return root
    left_parent = findParentNode(root.left, target)
    if left_parent is not None:
        return left_parent
    return findParentNode(root.right, target)
if __name__ == "__main__":
    
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    target = 5
    parent = findParentNode(root, target)
    if parent is not None:
        print(f"Parent of node {target} is {parent.val}")
    else:
        print(f"Node {target} not found or it is the root node")