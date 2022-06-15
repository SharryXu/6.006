from lec2 import ArraySeq


class TestArraySeq:
    def test_build(self):
        arr = ArraySeq()
        arr.build([1, 2, 3])
        assert len(arr) == 3
        assert arr.get_at(2) == 3

    def test_insert_at(self):
        arr = ArraySeq()

        arr.insert_at(0, 5)
        assert arr.get_at(0) == 5

        arr.insert_at(1, 10)
        assert arr.get_at(1) == 10

        arr.insert_at(20, 20)
        assert arr.get_at(1) == 10

    def test_delete_at(self):
        arr = ArraySeq()
        arr.build([1, 2, 3, 4, 5])

        arr.delete_at(8)
        assert arr.get_at(len(arr) - 1) == 5

        result = arr.delete_at(2)
        assert result == 3
        assert arr.get_at(2) == 4

    def test_set_at(self):
        arr = ArraySeq()
        arr.build([1, 2, 3])
        arr.set_at(0, 4)
        assert arr.get_at(0) == 4

    def test_insert_first(self):
        arr = ArraySeq()
        arr.build([1, 2, 3])
        arr.insert_first(5)
        assert len(arr) == 4
        assert arr.get_at(0) == 5

    def test_delete_first(self):
        arr = ArraySeq()
        arr.build([1, 2, 3])
        assert arr.delete_first() == 1
        assert len(arr) == 2

    def test_insert_last(self):
        arr = ArraySeq()
        arr.insert_last(3)
        assert len(arr) == 1
        assert arr.get_at(0) == 3

    def test_delete_last(self):
        arr = ArraySeq()
        arr.build([1, 2, 3])
        assert arr.delete_last() == 3
        assert len(arr) == 2
