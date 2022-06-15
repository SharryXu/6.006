#!/usr/bin/env python3

from os import getcwd
from sys import path

from rc_2_linked_list_seq import LinkedListSeq
from rc_2_set_from_seq import set_from_seq

path.append(getcwd() + "\\6.006\\lec2")

from random import randint


class HashTableSet:
    def __init__(self, r=200) -> None:
        self.chain_set = set_from_seq(LinkedListSeq)
        self.A = []
        self.size = 0
        self.r = r
        self.p = 2**31 - 1
        self.a = randint(1, self.p - 1)
        self._compute_bounds()
        self._resize(0)

    def _compute_bounds(self):
        self.upper = len(self.A)
        self.lower = len(self.A) * 100 * 100 // (self.r * self.r)

    def _resize(self, n):
        if (self.lower >= n) or (n >= self.upper):
            f = self.r // 100
            if self.r % 100:
                f += 1
            m = max(n, 1) * f

            # Re-Create hash table
            A = [self.chain_set() for _ in range(m)]
            for x in self:
                h = self._hash(x.key, m)
                A[h].insert(x)
            self.A = A
            self._compute_bounds()

    def _hash(self, k, m):
        return ((self.a * k) % self.p) % m

    def __len__(self):
        return self.size

    def __iter__(self):
        for x in self.A:
            yield from x

    def build(self, x):
        for i in x:
            self.insert(i)

    def find(self, k):
        h = self._hash(k, len(self.A))
        return self.A[h].find(k)

    def insert(self, x):
        self._resize(self.size + 1)
        h = self._hash(x.key, len(self.A))
        # print(f'key: {x.key}, hash: {h}')
        self.A[h].insert(x)
        self.size += 1

    def delete(self, k):
        h = self._hash(k, len(self.A))
        x = self.A[h].delete(k)
        if x is not None:
            self.size -= 1
            self._resize(self.size)
        return x

    def find_min(self):
        out = None
        for h in self.A:
            if len(h) > 0:
                for x in h:
                    if (out is None) or (x.key < out.key):
                        out = x
        return out

    def find_next(self, k):
        out = None
        for h in self.A:
            if len(h) > 0:
                for x in h:
                    if x.key > k:
                        if (out is None) or (x.key < out.key):
                            out = x
        return out

    def iter_order(self):
        x = self.find_min()
        while x:
            yield x
            x = self.find_next(x.key)


class Item:
    def __init__(self, key, value):
        self.key, self.value = key, value

    def __str__(self) -> str:
        return f"key: {self.key}, value: {self.value}"
