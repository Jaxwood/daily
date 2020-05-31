def intersect_node(a: [int], b: [int]) -> int:
    """Given two singly linked lists that intersect at some point, find the
    intersecting node. The lists are non-cyclical."""
    s = set(a)
    for i in b:
        if i in s:
            return i