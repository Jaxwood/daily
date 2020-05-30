import re


class Node:
    def __init__(self, val, children=[]):
        self.children = children
        self.val = val

    def len(self) -> int:
        return len(self.val)


def parse(s: str, separator: str = '\\n\\t') -> Node:
    res = re.split(separator+'(?!\\t)', s)
    children = []
    for i in res:
        if has_subdirectory(i):
            children.append(parse(i, separator + '\\t'))
        elif is_file(i):
            children.append(Node(i))
    return Node(res[0], children)


def has_subdirectory(s: str) -> bool:
    return s.find('\n\t') != -1


def is_file(s: str) -> bool:
    return s.find('.') != -1


def longest_path(n: Node) -> int:
    s = n.len()
    queue = []
    best = 0

    # initialize the queue
    for i in n.children:
        queue.append((i, s))

    # visit all nodes
    while len(queue) > 0:
        (q, t) = queue.pop(0)
        # add 1 for the directory separator, e.g. 'dir/subdir1'
        t += q.len() + 1
        best = max(t, best)
        for i in q.children:
            queue.append((i, t))

    return best


if __name__ == "__main__":
    s = parse(
        "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext")
    longest_path(s)
