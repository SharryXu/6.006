from ps_collage_collating import OttoShop


class TestCollageCollating():
    def test_make_document(self):
        shop = OttoShop()
        shop.make_document([1, 2, 3])
        result = shop.display()
        assert '2 -> 3' in result

    def test_move_below(self):
        shop = OttoShop()
        shop.make_document([1, 2, 3, 4, 5])
        shop.move_below(5, 3)
        result = shop.display()
        assert '2 -> 5 -> 3 -> 4' in result

