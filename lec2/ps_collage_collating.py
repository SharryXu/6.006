from .double_linked_list import DoubleLinkedList, DoubleLinkedListNode


class OttoShop:
    def make_document(self):
        self.set = []
        self.seq = DoubleLinkedList()

    def _binary_search(self, x, a=0, b=None):
        if b is None:
            b = len(self.set) - 1
        if a < b:
            c = (a + b) // 2 + 1
            if self.set[c].item == x:
                return c
            elif self.set[c].item < x:
                return self._binary_search(x, c + 1, b)
            else:
                return self._binary_search(x, a, c - 1)
        return a

    def _insert(self, x: DoubleLinkedListNode):
        i = self._binary_search(x.item)
        new_set = [None] * (len(self.set) + 1)
        for j in range(i):
            new_set[j] = self.set[j]
        new_set[i] = x
        for j in range(i + 1, len(new_set)):
            new_set[j] = self.set[j - 1]
        self.set = new_set

    def import_image(self, x):
        self.seq.insert_last(x)
        self._insert(self.seq.tail)

    def display(self):
        result = ""
        tail = self.seq.tail
        while tail is not None:
            result += f"{str(tail.item)} -> "
            tail = tail.prev
        return f"{result}None"

    def move_below(self, x, y):
        """
        move the image with ID x directly below the image with ID y
        """
        x_i, y_i = self._binary_search(x), self._binary_search(y)
        node_x: DoubleLinkedListNode = self.set[x_i]
        node_y: DoubleLinkedListNode = self.set[y_i]
        # delete x
        if node_x.prev is None:
            # head
            pass
        else:
            node_x.prev.next = node_x.next
            node_x.next.prev = node_x.prev
        # insert x before y
        tmp = node_y.prev
        node_y.prev.next = node_x
        node_y.prev = node_x
        node_x.prev = tmp
        node_x.next = node_y
