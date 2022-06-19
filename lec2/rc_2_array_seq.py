#!/usr/bin/env python3

"""
Index is start with 0
"""


class ArraySeq:
    def __init__(self) -> None:
        self.A = []
        self.size = 0

    def __len__(self) -> int:
        return self.size

    def __iter__(self):
        yield from self.A

    def build(self, x):
        self.A = [a for a in x]
        self.size = len(self.A)

    def get_at(self, i):
        return self.A[i]

    def set_at(self, i, x):
        self.A[i] = x

    def _copy_forward(self, i: int, n: int, B: list, j: int) -> None:
        """
        Copy array A to array B

        :parm i:
            index of array A

        :parm n:
            copy count

        :parm B:
            array B

        :parm j:
            index of array B
        """
        for k in range(n):
            B[j + k] = self.A[i + k]

    def _copy_backward(self, i: int, n: int, B: list, j: int) -> None:
        """
        Copy array A to array B

        :parm i:
            index of array A

        :parm n:
            copy count

        :parm B:
            array B

        :parm j:
            index of array B
        """

        for k in range(n - 1, -1, -1):
            B[j + k] = self.A[i + k]

    def insert_at(self, i, x):
        n = len(self.A)
        if i > n:
            return
        new_A = [None] * (n + 1)
        self._copy_forward(0, i, new_A, 0)
        new_A[i] = x
        self._copy_forward(i, n - i, new_A, i + 1)
        self.build(new_A)

    def delete_at(self, i):
        n = len(self.A)
        if i >= n:
            return
        x = self.A[i]
        new_A = [None] * (n - 1)
        self._copy_forward(0, i, new_A, 0)
        self._copy_forward(i + 1, n - i - 1, new_A, i)
        self.build(new_A)
        return x

    def insert_first(self, x):
        self.insert_at(0, x)

    def delete_first(self):
        return self.delete_at(0)

    def insert_last(self, x):
        self.insert_at(len(self), x)

    def delete_last(self):
        return self.delete_at(len(self) - 1)

    def print(self):
        for i in self.A:
            print(i, end=" ")
        print()
