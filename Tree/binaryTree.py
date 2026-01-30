
class Node:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

def in_order_traversal(root: Node):
    if root is not None:
        in_order_traversal(root.left)
        print(root.val)
        in_order_traversal(root.right)
def pre_order_traversal(root: Node):
    if root is not None:
        print(root.val)
        pre_order_traversal(root.left)
        pre_order_traversal(root.right)
def posrt_order_traversal(root: Node):
    if root is not None:
        posrt_order_traversal(root.left)
        posrt_order_traversal(root.right)
        print(root.val)
def build_tree(nodes, f):


    
    val = next(nodes)
    if val == 'N' :
        return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

if __name__ == "__main__":
    root = build_tree(iter(input().split()),int)
    pre_order_traversal(root)
    print("-----")
    posrt_order_traversal(root)
    print("-----")
    in_order_traversal(root)