

class Node:
    def __init__(self, val):
        self.val = val
        self.left =None
        self.right =None

def maxDepth(root: Node) :
    if root is None:
        return 0
    else:
        LeftDepth = maxDepth(root.left)
        RightDepth = maxDepth(root.right)
        return max(LeftDepth, RightDepth) + 1
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print(maxDepth(root))