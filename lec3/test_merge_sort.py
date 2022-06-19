from random import randint

from test_selection_sort import verify_sequence

from .merge_sort import (
    merge_sort,
    merge_two_array_1,
    merge_two_array_2,
    merge_two_array_3,
)


class TestMergeSort:
    def test(self):
        arr = [randint(1, 30) for _ in range(30)]
        merge_sort(arr)
        verify_sequence(arr)

    def test_merge_two_array(self):
        arr = [2, 4, 1, 3]
        L = arr[0:2]
        R = arr[2:4]
        merge_two_array_1(arr, L, R, 1, 3)
        verify_sequence(arr)

    def test_merge_two_array_2(self):
        arr = [2, 4, 1, 3, 5]
        L = arr[0:2]
        R = arr[2:5]
        merge_two_array_2(arr, L, R, 1, 4, len(L) - 1, len(R) - 1)
        verify_sequence(arr)

    def test_merge_two_array_3(self):
        arr = [1, 2, 4, 3, 5]
        L = arr[0:3]
        R = arr[3:5]
        merge_two_array_3(arr, L, R, 2, 4, len(L) - 1, len(R) - 1)
        verify_sequence(arr)
