from random import randint

from radix_sort import radix_sort


class TestRadixSort:
    def test(self):
        A = [randint(10, 1000) for i in range(30)]
        A = radix_sort(A)
        for i in range(len(A) - 1):
            assert A[i] <= A[i + 1]
