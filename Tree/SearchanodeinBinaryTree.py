
class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
def searchNode(root:Node, target):
    if root is None:
        return False
    if root.val == target:
        return True
    return searchNode(root.left, target) or searchNode(root.right, target)
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    target = 100
    if searchNode(root, target):
        print(f"Node {target} found in the tree")
    else:
        print(f"Node {target} not found in the tree")