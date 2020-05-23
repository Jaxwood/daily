class Node:
    def __init__(self, nodes, done):
        self.nodes = nodes
        self.done = done
    
def autocomplete(trie, word):
    """
    Implement an autocomplete system. That is, given a query string s and a
    set of all possible query strings, return all strings in the set that
    have s as a prefix. For example, given the query string de and the set of
    strings [dog, deer, deal], return [deer, deal].
    """
    w = word
    n = trie
    while len(w) > 0:
        n = n.nodes[w[:1]]
        w = w[1:]
    
    result = []
    queue = [(i, word, n.nodes[i]) for i in n.nodes]
    for (a,b,m) in queue:
        if m.done:
            for i in m.nodes:
                if i:
                    result.append(b+a+i)
        else:
            next = [(i, b+a, m.nodes[i]) for i in m.nodes]
            queue += next

    return result
