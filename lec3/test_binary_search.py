from binary_search import binary_search


class TestBinarySearch:
    def test_exist(self):
        arr = [1, 2, 3, 4, 5]
        assert binary_search(arr, 3) == 2

        arr = [1]
        assert binary_search(arr, 1) == 0

        arr = [1, 2]
        assert binary_search(arr, 2) == 1

    def test_not_exist(self):
        arr = [1, 2, 3, 4]
        assert binary_search(arr, 6) == None

        arr = [1]
        assert binary_search(arr, 0) == None
