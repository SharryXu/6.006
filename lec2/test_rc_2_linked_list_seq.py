from rc_2_linked_list_seq import LinkedListSeq


class TestLinkedListSeq:
    def test_build(self):
        seq = LinkedListSeq()
        seq.build([1, 2, 3])
        assert seq.get_at(0) == 1
        assert seq.get_at(2) == 3

    def test_insert_first(self):
        seq = LinkedListSeq()
        seq.insert_first(6)
        assert seq.get_at(0) == 6
        assert len(seq) == 1

    def test_delete_first(self):
        empty_seq = LinkedListSeq()
        assert empty_seq.delete_first() == None

        seq = LinkedListSeq()
        seq.build([1, 2, 3])
        assert seq.delete_first() == 1
        assert len(seq) == 2

    def test_insert_last(self):
        seq = LinkedListSeq()
        seq.insert_last(3)
        assert len(seq) == 1
        assert seq.get_at(0) == 3

    def test_delete_last(self):
        seq = LinkedListSeq()
        seq.build([1, 2, 3])
        assert seq.delete_last() == 3
        assert len(seq) == 2
        assert seq.get_at(1) == 2
