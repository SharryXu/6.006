from lec3.test_selection_sort import verify_sequence
from lec5.direct_access_sort import direct_access_sort


class TestDirectAccessSort:
    def test(self):
        arr = [3, 1, 4, 8, 2, 6]
        direct_access_sort(arr)
        verify_sequence(arr)

        arr = [3, 1]
        direct_access_sort(arr)
        verify_sequence(arr)
