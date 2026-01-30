import sys

class Node:
    def __init__(self, val):
        self.val = val
        self.children = []

def add_child(parent: Node, child: Node):
    parent.children.append(child)

def print_parents(node,parent):
    if parent is None:
        print(f"{node.val} ----> NULL")
    else:
        print(f"{node.val} ----> {parent.val}")
    for child in node.children:
        print_parents(child, node)

def print_children(node: Node):
    if not node.children:
        print(f"{node.val} ----> NULL")
    else:
        children_vals = ', '.join(str(child.val) for child in node.children)
        print(f"{node.val} ----> {children_vals}")
    for child in node.children:
        print_children(child)
def print_leafNode(node: Node):
    if not node.children:
        print(f"{node.val} is a leaf node")
    for child in node.children:
        print_leafNode(child)
if __name__ == "__main__":
    root = Node(1)
    child1 = Node(2)
    child2 = Node(3)
    child3 = Node(4)
    child4 = Node(5)
    
    add_child(root, child1)
    add_child(root, child2)
    add_child(child2, child3)
    add_child(child3, child4)

    print_parents(root, None)
    print("-----")
    print_children(root)
    print("-----")
    print_leafNode(root)