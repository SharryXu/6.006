from .double_linked_list import *


class TestDoubleLinkedList:
    def test_insert_last(self):
        l = DoubleLinkedList()
        l.insert_last(3)
        l.insert_last(4)
        l.insert_last(5)
        l.insert_last(6)
        result = ""
        for i in l:
            result += f"{str(i.item)}->"
        result += "None"
        assert "3->4->5->6->None" in result
