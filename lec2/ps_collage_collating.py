from rc_2_linked_list_seq import LinkedListSeq


class OttoShop:
    def make_document(self, x):
        self.set = []
        self.seq = LinkedListSeq()
        for i in x:
            self.seq.insert_last(i)
            self.set.append(self.seq.get_latest_node())

    def import_image(self, x):
        self.seq.insert_last(x)
        self.set.append(self.seq.get_latest_node())

    def display(self):
        result = ""
        for i in self.seq:
            result += f"{str(i)} -> "
        return f"{result}None"

    def move_below(self, x, y):
        pass
