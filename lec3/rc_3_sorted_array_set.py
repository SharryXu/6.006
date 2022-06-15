#!/usr/bin/env python3


from ..lec2.rc_2_array_seq import ArraySeq


class SortedArraySet:
    def __init__(self):
        self.A = ArraySeq()

    def __len__(self):
        return len(self.A)

    def __iter__(self):
        yield from self.A

    def iter_order(self):
        yield from self

    def build(self, x):
        self.A.build(x)
        self._sort_insertion()

    def _swap(self, i, j):
        tmp = self.A.get_at(i)
        self.A.set_at(i, self.A.get_at(j))
        self.A.set_at(j, tmp)

    def _sort_insertion(self, i=None):
        if i is None:
            i = len(self) - 1
        if i > 0:
            j = self._sort_prefix_max(i)
            self._swap(i, j)
            self._sort_insertion(i - 1)

    def _sort_prefix_max(self, i):
        if i > 0:
            j = self._sort_prefix_max(i - 1)
            if self.A.get_at(j).key > self.A.get_at(i).key:
                return j
        return i

    def _binary_search(self, x, a=0, b=None):
        # instead of returning None, we return i, this is because of the insert method.
        if b is None:
            b = len(self) - 1
        if a < b:
            c = (a + b) // 2
            if self.A.get_at(c).key < x:
                return self._binary_search(x, c + 1, b)
            elif self.A.get_at(c).key > x:
                return self._binary_search(x, a, c - 1)
            else:
                return c
        return a

    def find_main(self):
        if len(self) > 0:
            return self.A.get_at(0)
        else:
            return None

    def find_max(self):
        if len(self) > 0:
            return self.A.get_at(len(self) - 1)
        else:
            return None

    def find(self, k):
        i = self._binary_search(k)
        r = self.A.get_at(i)
        if r.key == k:
            return r
        else:
            return None

    def insert(self, x):
        if len(self.A) == 0:
            self.A.insert_first(x)
        else:
            i = self._binary_search(x)
            k = self.A.get_at(i).key
            if k == x.key:
                self.A.set_at(i, x)
                return False
            elif k > x.key:
                self.A.insert_at(i, x)
            else:
                self.A.insert_at(i + 1, x)

    def delete(self, k):
        i = self._binary_search(k)
        assert self.A.get_at(i).key == k
        return self.A.delete_at(i)


class Item:
    def __init__(self, key, value):
        self.key = key
        self.value = value
