class Node:
    """Given a singly linked list and an integer k, remove the kth last
    element from the list. k is guaranteed to be smaller than the length of
    the list."""

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        current_node = self
        result = []
        while current_node:
            result.append(current_node.val)
            current_node = current_node.next
        return str(result)


def remove(head, k):
    slow, fast = head, head
    for _ in range(k):
        fast = fast.next

    prev = None
    while fast:
        prev = slow
        slow = slow.next
        fast = fast.next

    prev.next = slow.next
