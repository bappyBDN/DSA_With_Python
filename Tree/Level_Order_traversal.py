
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
def Level_Order_traversal(root:Node, level, result):
    if root is None:
        return
    if level == len(result):
        result.append([])
    result[level].append(root.value)
    Level_Order_traversal(root.left, level + 1, result)
    Level_Order_traversal(root.right, level + 1,
                           result)
def print_Level_Order_traversal(root:Node):
    result = []
    Level_Order_traversal(root, 0, result)
    for level in result:
        print(" ".join(str(x) for x in level))
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    print_Level_Order_traversal(root)