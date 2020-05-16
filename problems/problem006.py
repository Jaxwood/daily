class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class XORLinkedList:

    def __init__(self):
        self.head = None

    def dereference_pointer(self):
        pass

    def get_pointer(self):
        pass

    def get(self, index):
        cnt = 0
        n = self.head
        while cnt != index:
            n = n.next
            cnt += 1
        
        return n.data

    def add(self, element):
        n = Node(element)
        n.next = None

        if self.head is None:
            n.prev = None
            self.head = n
            return

        last = self.head
        while last.next is not None:
            last = last.next

        last.next = n
        n.prev = last
        return
