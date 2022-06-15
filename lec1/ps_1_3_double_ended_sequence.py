#!/usr/bin/env python3

"""
design a data structure to store a sequence of items that supports worst-case O(1)-time 
index lookup, as well as amortized O(1)-time insertion and removal at both ends.
Your data structure should use O(n) space to store n items.
"""

from lec2 import ArraySeq, DynamicArraySeq


class LeftDynamicArraySeq(ArraySeq):
    def __init__(self, r=2) -> None:
        super().__init__()
        self.r = r
        self.size = 0
        self.first_index = 0
        self._compute_bounds()
        self._resize(0)

    def _compute_bounds(self):
        self.upper = len(self.A)
        self.lower = len(self.A) // self.r

    def _resize(self, s):
        if self.lower < s * 2 < self.upper:
            return None
        size_of_b = max(s, 1) * self.r
        b = [None] * size_of_b
        self._copy_forward(self.first_index, self.size, b, size_of_b // 2)
        self.A = b
        self.first_index = self._real_size() // 2
        self._compute_bounds()

    def _real_size(self):
        return len(self.A)

    def __len__(self) -> int:
        return self.size

    def get_at(self, i):
        return self.A[self.first_index + i]

    def set_at(self, i, x):
        self.A[self.first_index + i] = x

    def insert_at(self, i, x):
        if i == 0:
            self.insert_first(x)
            return True
        else:
            if i > self.first_index + self.size:
                return False
            else:
                self.A[self.first_index + i] = x
                self.size += 1
                return True

    def insert_first(self, x):
        # insert_first operation will resize array.
        self._resize(self.size + 1)
        self.A[self.first_index - 1] = x
        self.first_index -= 1
        self.size += 1

    def insert_last(self, x):
        # insert_first operation will NOT resize array.
        if self.first_index + self.size <= self._real_size():
            self.A[self.first_index + self.size] = x
            self.size += 1
            return True
        return False

    def delete_first(self):
        if len(self) is 0:
            return None
        x = self.A[self.first_index]
        self.size -= 1
        self._copy_forward(self.first_index + 1, self.size, self.A, self.first_index)
        self._resize(self.size)
        return x

    def delete_last(self):
        x = self.A[self.first_index + self.size - 1]
        self.size -= 1
        self._resize(self.size)
        return x

    def build(self, x):
        for i in x:
            # Build operation will resize array.
            self._resize(self.size + 1)
            self.insert_last(i)

    def __iter__(self):
        for i in range(self.size):
            yield self.A[self.first_index + i]


class RightDynamicArraySeq(DynamicArraySeq):
    def __init__(self, r=2) -> None:
        super().__init__(r)


class DoubleEndedSeq:
    def __init__(self) -> None:
        self.left = LeftDynamicArraySeq()
        self.right = RightDynamicArraySeq()

    def build(self, x):
        L = x[: len(x) // 2 + 1]
        R = x[len(x) // 2 + 1 :]
        self.left.build(L)
        self.right.build(R)

    def __len__(self):
        return len(self.left) + len(self.right)

    def __iter__(self):
        # left
        for i in range(-len(self.len), -1, -1):
            yield self.left[i]
        # right
        for j in range(len(self.right)):
            yield self.right[j]

    def get_at(self, i):
        if i < 0 or i > len(self):
            return None
        if i < len(self.left):
            return self.left.get_at(i)
        else:
            return self.right.get_at(i - len(self.left))

    def set_at(self, i, x):
        if i < len(self.left):
            self.left.set_at(i, x)
        else:
            self.right.set_at(i - len(self.left), x)

    def insert_first(self, x):
        self.left.insert_first(x)

    def insert_last(self, x):
        self.right.insert_last(x)

    def delete_first(self):
        result = self.left.delete_first()
        if result is None:
            return self.right.delete_first()
        else:
            return result

    def delete_last(self):
        result = self.right.delete_last()
        if result is None:
            return self.left.delete_last()
        else:
            return result
