class Node:
    """Given the root to a binary tree, implement serialize(root),
    which serializes the tree into a string, and deserialize(s),
    which deserializes the string back into the tree."""

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(node):
    """serialize as a lisp list"""
    left = serialize(node.left) if node.left else "()"
    right = serialize(node.right) if node.right else "()"
    return "({0}{1}{2})".format(node.val, left, right)


def deserialize(nodestr):
    """deserialize the lisp list into a Node"""
    # strip outer parentese
    s = nodestr[1:][:-1]
    # find current value
    i = s.find('(')
    val = s[:i]
    res = segment(s[i:])
    return Node(val, deserialize(res[0]), deserialize(res[1])) if val else None


def segment(nodestr):
    """get the left and right nodes"""
    cnt = 0
    res = []
    start = 0
    for a in range(len(nodestr)):
        if nodestr[a] == '(':
            cnt += 1
        elif nodestr[a] == ')':
            cnt -= 1
        if cnt == 0:
            res.append(nodestr[start:][:a + 1])
            start = a + 1
    return res
