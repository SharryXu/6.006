from lec3.test_selection_sort import verify_sequence
from lec5.counting_sort import counting_sort


class TestCountingSort:
    def test(self):
        arr = [3, 8, 4, 8, 2, 6]
        counting_sort(arr)
        verify_sequence(arr)

        arr = [3, 1]
        counting_sort(arr)
        verify_sequence(arr)
