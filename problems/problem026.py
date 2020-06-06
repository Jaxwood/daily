class Node:
    """Given a singly linked list and an integer k, remove the kth last
    element from the list. k is guaranteed to be smaller than the length of
    the list."""

    def __init__(self, val: int, n = None):
        self.val = val
        self.next = n

    def remove(self, k: int):
        l = self.length()
        n = self
        cnt = 1
        until = l - k - 1
        if until == 0:
            return self.next
        while until != cnt:
            cnt += 1
            n = n.next

        if k == 0:
            n.next = None
        else:
            n.next = n.next.next
        return self

    def length(self):
        l = 1
        n = self.next
        while n:
            l += 1
            n = n.next
        return l
