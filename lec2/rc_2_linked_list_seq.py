#!/usr/bin/env python3

class LinkedListNode:
    def __init__(self, x) -> None:
        self.item = x
        self.next = None

    def later_node(self, i) -> object:
        if i == 0:
            return self
        assert self.next
        return self.next.later_node(i - 1)
    
    def __str__(self) -> str:
        return f'({self.item})'

class LinkedListSeq:
    def __init__(self) -> None:
        self.head: LinkedListNode = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        node: LinkedListNode = self.head
        while node:
            yield node.item
            node = node.next

    def build(self, x):
        for i in reversed(x):
            self.insert_first(i)

    def insert_first(self, x):
        node = LinkedListNode(x)
        node.next = self.head
        self.head = node
        self.size += 1

    def delete_first(self):
        if self.head is None:
            return
        x = self.head.item
        self.head = self.head.next
        self.size -= 1
        return x

    def set_at(self, i, x):
        node = self.head.later_node(i)
        node.item = x

    def get_at(self, i):
        node = self.head.later_node(i)
        return node.item
    
    def get_node_at(self, i):
        return self.head.later_node(i)
 
    def get_latest_node(self):
        return self.head.later_node(self.size - 1)

    def insert_at(self, i, x):
        if i == 0:
            self.insert_first(x)
            return
        n = min(i, self.size) - 1
        new_node = LinkedListNode(x)
        node = self.head.later_node(n)
        new_node.next = node.next
        node.next = new_node
        self.size += 1

    def delete_at(self, i):
        if i == 0:
            self.delete_first()
            return
        node = self.head.later_node(i - 1)
        x = node.next.item
        node.next = node.next.next
        self.size -= 1
        return x

    def insert_last(self, x):
        self.insert_at(self.size, x)

    def delete_last(self):
        return self.delete_at(self.size - 1)
