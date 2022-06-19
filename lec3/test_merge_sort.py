from random import randint

from test_selection_sort import verify_sequence

from .merge_sort import merge_sort


class TestMergeSort:
    def test(self):
        arr = [randint(1, 30) for _ in range(30)]
        merge_sort(arr)
        verify_sequence(arr)
