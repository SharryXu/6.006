from random import randint

from selection_sort import prefix_max, selection_sort


class TestSelectionSort:
    def test_prefix_max(self):
        arr = [8, 2, 4, 9, 3]
        assert prefix_max(arr) == 3
        assert prefix_max(arr, 2) == 0
        assert prefix_max(arr, 3) == 3
        assert prefix_max(arr, 4) == 3

    def test_selection_sort(self):
        arr = [randint(1, 30) for _ in range(30)]
        selection_sort(arr)
        self.verify_sequence(arr)

        arr = [0, 1, 0, 2, 1]
        selection_sort(arr)
        self.verify_sequence(arr)

    @staticmethod
    def verify_sequence(arr):
        for i in range(len(arr) - 1):
            assert arr[i] <= arr[i + 1]
