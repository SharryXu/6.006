#!/usr/bin/env python

class ListNode():
    def __init__(self, value) -> None:
        self.value = value
        self.prev = None
        self.next = None


class CycleList():
    def __init__(self):
        self.head = None
        self.size = 0

    def build(self, x):
        self.size = 0
        self.head = None
        for i in x:
            self.insert_last(i)

    def insert_last(self, x):
        node = ListNode(x)
        if self.size == 0:
            node.prev = node
            node.next = node
            self.head = node
            self.size += 1
        else:
            prev = self.head.prev
            cur = self.head

            node.prev = prev
            prev.next = node
            node.next = cur
            cur.prev = node
            self.size += 1

    def count_node(self):
        slow = self.head
        fast = self.head
        collide = None
        while True:
            slow = slow.next
            fast = fast.next.next
            if slow.value == fast.value and slow.prev == fast.prev and slow.next == fast.next:
                collide = slow
                break
        node = collide
        count = 0
        while True:
            node = node.next
            if node.value == collide.value and node.prev == collide.prev and node.next == collide.next:
                break
            else:
                count += 1
        return count + 1
