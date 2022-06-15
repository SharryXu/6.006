from ps_1_3_double_ended_sequence import DoubleEndedSeq


class TestDoubleEndedSeq:
    def test_build(self):
        seq = DoubleEndedSeq()
        seq.build([1, 2, 3, 4, 5])
        assert seq.get_at(-1) == None
        assert seq.get_at(0) == 1
        assert seq.get_at(1) == 2
        assert seq.get_at(2) == 3
        assert seq.get_at(3) == 4
        assert seq.get_at(4) == 5
        assert seq.get_at(5) == None
        # assert seq.get_at(4) == 5

        seq = DoubleEndedSeq()
        assert seq.get_at(0) == None
        assert seq.get_at(-1) == None

    def test_insert_first(self):
        seq = DoubleEndedSeq()
        seq.build([1, 2, 3, 4, 5])
        seq.insert_first(8)
        seq.insert_first(9)
        assert seq.get_at(0) == 9
        assert seq.get_at(1) == 8
        assert seq.get_at(2) == 1

    def test_insert_last(self):
        seq = DoubleEndedSeq()
        seq.build([1, 2, 3, 4, 5])
        seq.insert_last(8)
        seq.insert_last(9)
        assert seq.get_at(5) == 8
        assert seq.get_at(6) == 9

    def test_delete_first(self):
        seq = DoubleEndedSeq()
        seq.build([1, 2, 3, 4, 5])
        assert seq.delete_first() == 1
        assert seq.delete_first() == 2
        assert len(seq) == 3
        assert seq.delete_first() == 3
        assert seq.delete_first() == 4
        assert seq.delete_first() == 5
        assert len(seq) == 0

    def test_delete_last(self):
        seq = DoubleEndedSeq()
        seq.build([1, 2, 3, 4, 5])
        assert seq.delete_last() == 5
        assert seq.delete_last() == 4
        assert len(seq) == 3
        assert seq.delete_last() == 3
        assert seq.delete_last() == 2
        assert seq.delete_last() == 1
        assert len(seq) == 0
