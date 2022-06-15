from ps_1_4_jen_berry import *


class TestJenBerry:
    def test_build(self):
        seq = LinkedList()
        seq.build([1, 4, 5, 8, 7])
        assert len(seq) == 5

    def test_iter(self):
        seq = LinkedList()
        seq.build([1, 4, 5, 8, 7])
        print_result = ""
        for i in seq:
            print_result += str(i)
        assert len(print_result) > 0

    def test_reverset_at(self):
        seq = JenBerryList()
        seq.build(["sharry", "john", "nick", "olly", "tony", "dana"])
        seq.reverse_at(len(seq) // 2)
        print_result = ""
        for i in seq:
            print_result += str(i)
        assert len(print_result) > 0
