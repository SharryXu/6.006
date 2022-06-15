from rc_2_dynamic_array_seq import DynamicArraySeq


class TestDynamicArraySeq:
    def test_build(self):
        arr = DynamicArraySeq()
        assert arr._real_size() == 2
        assert len(arr) == 0

    def test_dynamic(self):
        arr = DynamicArraySeq()
        arr.build([1, 2, 3])
        assert arr._real_size() == 4
        assert len(arr) == 3

        arr.insert_last(4)
        arr.insert_last(5)
        assert arr._real_size() == 8
        assert len(arr) == 5

        assert arr.delete_last() == 5
        assert arr.delete_last() == 4
        assert arr.delete_last() == 3
        assert arr.delete_last() == 2

        assert arr._real_size() == 2
        assert len(arr) == 1

    def test_insert_at(self):
        arr = DynamicArraySeq()
        arr.insert_at(3, 4)
        assert len(arr) == 0

        arr.insert_at(0, 4)
        arr.get_at(0)
        assert len(arr) == 1
