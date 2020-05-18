class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def equal(node):
    if node.left and node.right:
        return node.left.val == node.right.val == node.val
    return False

def unival(tree, cnt=0):
    """Given the root to a binary tree, count the number of unival subtrees"""
    # is it a leaf?
    if tree.right == tree.left == None:
        return cnt + 1
    # sum rest of the tree
    return unival(tree.left, cnt + 1 if equal(tree) else cnt) + unival(tree.right, cnt)
