from random import randint

from insertion_sort import insertion_sort
from test_selection_sort import verify_sequence


class TestInsertionSort:
    def test(self):
        arr = [randint(1, 30) for _ in range(30)]
        insertion_sort(arr)
        verify_sequence(arr)
