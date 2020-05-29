class Node:
  def __init__(self, val, children = []):
    self.children = children
    self.val = val

def parse(s: str) -> Node:
  return Node("dir", [Node("subdir1", [Node("file1.ext"), Node("tsubsubdir1")]), Node("subdir2", [Node("subsubdir2", [Node("file2.ext")])])])

def longest_path(ns: Node) -> int:
  s = len(ns.val)
  queue = []
  best = 0

  # initialize the queue
  for i in ns.children:
    queue.append((i,s))

  # visit all nodes
  while len(queue) > 0:
    (q, t) = queue.pop(0)
    # add 1 for the directory separator, e.g. 'dir/subdir1'
    t += len(q.val) + 1
    best = max(t, best)
    for i in q.children:
      queue.append((i, t))
  
  return best


# "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"

# "dir
#   subdir1\n\t\tfile1.ext\n\t\tsubsubdir1
#   subdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"

# "dir
#   subdir1
#     file1.ext
#     tsubsubdir1
#   subdir2
#     subsubdir2\n\t\t\tfile2.ext"

#  Node(dir, [Node(subdir1, [Node(file1.ext), Node(tsubsubdir1)]), Node(subdir2, [Node(subsubdir2, [Node(file2.ext")])])])]