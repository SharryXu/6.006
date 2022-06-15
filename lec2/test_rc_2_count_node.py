from rc_2_count_node import CycleList


class TestCountNode():
    def test_count_node(self):
        cycle = CycleList()
        cycle.build([1, 2, 3, 4, 5, 6])
        assert cycle.count_node() == 6

        cycle.build([x for x in range(20)])
        assert cycle.count_node() == 20
