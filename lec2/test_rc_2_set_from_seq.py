from rc_2_array_seq import ArraySeq
from rc_2_set_from_seq import set_from_seq


class Item:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value


class TestRC2SetFromSeq:
    def test_build(self):
        s = set_from_seq(ArraySeq)
