from random import randint

from tuple_sort import tuple_sort


class TestTupleSort:
    def test(self):
        A = [randint(10, 100) for i in range(10)]
        tuples = [divmod(i, 10) for i in A]
        tuples = tuple_sort(tuples)
        for i in range(len(tuples) - 1):
            assert (
                tuples[i][0] * 10 + tuples[i][1]
                <= tuples[i + 1][0] * 10 + tuples[i + 1][1]
            )
