"""Given the root of a binary tree, determine if it is height-balanced. A binary tree is considered height-balanced if the absolute difference in heights of the left and right subtrees is at most 1 for every node in the tree."""
class Node :
    def __init__(self, val):
        self.val = val
        self.left =None
        self.right =None
def hight(node):
    if node is None:
        return 0
    return max(hight(node.left),hight(node.right))+1

def isBalanced(root):
    if root is None:
        return True
    lh= hight(root.left)
    rg= hight(root.right)
    if abs(lh - rg) <= 1 and isBalanced(root.left) and isBalanced(root.right):
        return True
    return False
if __name__ == "__main__":
    # Constructing a balanced binary tree
    #         1
    #        / \
    #       2   3
    #      / \
    #     4   5
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    if isBalanced(root):
        print("The tree is balanced")
    else:
        print("The tree is not balanced")

    # Constructing an unbalanced binary tree
    #         1
    #        /
    #       2
    #      /
    #     3
    root_unbalanced = Node(1)
    root_unbalanced.left = Node(2)
    root_unbalanced.left.left = Node(3)

    if isBalanced(root_unbalanced):
        print("The tree is balanced")
    else:
        print("The tree is not balanced")
