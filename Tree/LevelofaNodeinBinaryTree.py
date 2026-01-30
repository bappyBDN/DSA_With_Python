
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
def getLevel(root:Node, target, level):
    if root is None:
        return 0
    if root.val == target:
        return level
    left_level = getLevel(root.left,target,level+1)
    if left_level != 0:
        return left_level
    return getLevel(root.right,target,level+1)
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    target = 5
    level = getLevel(root,target,1)
    if level != 0:
        print(f"Level of node {target} is {level}")
    else:
        print(f"Node {target} not found in the tree")