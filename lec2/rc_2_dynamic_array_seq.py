#!/usr/bin/env python3


from lec2.rc_2_array_seq import ArraySeq


class DynamicArraySeq(ArraySeq):
    def __init__(self, r=2) -> None:
        super().__init__()
        self.size = 0
        self.r = r
        self._compute_bounds()
        self._resize(0)

    def _resize(self, n):
        # Hit Upper or Lower
        if self.lower < n < self.upper:
            return
        m = max(n, 1) * self.r
        A = [None] * m
        self._copy_forward(0, self.size, A, 0)
        self.A = A
        self._compute_bounds()

    def _real_size(self):
        """
        Just for test purpose
        """
        return len(self.A)

    def _compute_bounds(self):
        self.upper = len(self.A)
        self.lower = len(self.A) // self.r

    def __len__(self) -> int:
        return self.size

    def __iter__(self):
        for i in range(len(self)):
            yield self.A[i]

    def build(self, x):
        for a in x:
            self.insert_last(a)

    def insert_last(self, x):
        self._resize(self.size + 1)
        self.A[self.size] = x
        self.size += 1

    def delete_last(self):
        if len(self) is 0:
            return None
        x = self.A[self.size - 1]
        self.A[self.size - 1] = None
        self.size -= 1
        self._resize(self.size)
        return x

    def insert_at(self, i, x):
        if self.size < i:
            return
        self.insert_last(None)
        self._copy_backward(i, self.size - (i + 1), self.A, i + 1)
        self.A[i] = x

    def delete_at(self, i):
        """
        So that you can re-use delete_last method
        """
        x = self.A[i]
        self._copy_forward(i + 1, self.size - (i + 1), self.A, i)
        self.delete_last()
        return x

    def insert_first(self, x):
        self.insert_at(0, x)

    def delete_first(self):
        return self.delete_at(0)
