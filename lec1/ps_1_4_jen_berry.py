#!/usr/bin/env python3

"""
Problem Session 1

Jen & Berry
"""


class LinkedListNode:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

    def __str__(self) -> str:
        end = ""
        if self.next is None:
            end = "None"
        return f"({self.value}) -> {end}"


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def build(self, x):
        for i in x:
            self.insert_last(i)

    def insert_first(self, x):
        new_node = LinkedListNode(x)
        new_node.next = self.head
        self.size += 1
        self.head = new_node

    def insert_last(self, x):
        if self.size == 0:
            self.insert_first(x)
        else:
            end_node = self.head
            for _ in range(self.size - 1):
                end_node = end_node.next
            new_node = LinkedListNode(x)
            new_node.next = None
            end_node.next = new_node
            self.size += 1

    def __iter__(self):
        head = self.head
        for _ in range(self.size):
            yield head
            head = head.next


class JenBerryList(LinkedList):
    def reverse_at(self, i):
        n = len(self)
        if i > n - 2:
            # meaning less
            return
        a = self.head
        for _ in range(i - 1):
            a = a.next
        b = a.next
        # Use 2 new pointer to replace!!!!
        prev, cur = a, b
        for _ in range(n - i):
            next = cur.next
            cur.next = prev
            prev, cur = cur, next
        a.next = prev
        b.next = None
