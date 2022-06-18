class DoubleLinkedListNode(object):
    def __init__(self, value) -> None:
        self.item = value
        self.prev = None
        self.next = None


class DoubleLinkedList(object):
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def insert_last(self, x):
        node = DoubleLinkedListNode(x)
        if self.head is None:
            self.head = self.tail = node
            node.prev = None
            node.next = self.tail
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.size += 1

    def __iter__(self):
        head = self.head
        while head is not None:
            yield head
            head = head.next
