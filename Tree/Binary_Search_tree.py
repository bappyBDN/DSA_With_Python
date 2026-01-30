
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
def bst(root,key):
    if root is None:
        return Node(key)
    if root.val == key:
        return root
    if key <root.val:
        root.left = bst(root.left,key)
    else:
        root.right = bst(root.right,key)
        return root
def search(root,key):
    parent=False

    while root is not None:
        if root.val == key:
            parent=True
            break

        elif key < root.val:
            
            root = root.left
        else:
           
            root = root.right
    return parent
if __name__ == "__main__":
    root = None
    keys = [15,10,20,8,12,17,25]
    for key in keys:
        #root = bst(root,key)
        if not search(root,key):
            root = bst(root,key)
    print("Binary Search Tree created with root value:", root.val)