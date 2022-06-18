from .ps_collage_collating import OttoShop


class TestCollageCollating:
    def test_binary_search(self):
        shop = OttoShop()
        shop.make_document()
        shop.import_image(9)
        shop.import_image(7)
        shop.import_image(5)
        shop.import_image(3)
        shop.import_image(1)
        assert shop._binary_search(1) == 0
        assert shop._binary_search(7) == 3
        assert shop._binary_search(6) == 3
        assert shop._binary_search(0) == 0
        assert shop._binary_search(4) == 2

    def test_move_below(self):
        shop = OttoShop()
        shop.make_document()
        shop.import_image(5)
        shop.import_image(4)
        shop.import_image(3)
        shop.import_image(2)
        shop.import_image(1)
        shop.move_below(3, 5)
        result = shop.display()
        assert "1 -> 2 -> 4 -> 5 -> 3" in result

    def test_move_below_2(self):
        shop = OttoShop()
        shop.make_document()
        shop.import_image(5)
        shop.import_image(4)
        shop.import_image(3)
        shop.import_image(2)
        shop.import_image(1)
        shop.move_below(5, 3)
        result = shop.display()
        assert "1 -> 2 -> 3 -> 5 -> 4" in result
