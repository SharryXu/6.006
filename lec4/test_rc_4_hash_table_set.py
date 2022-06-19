from rc_4_hash_table_set import HashTableSet, Item


class TestHashTableSet:
    def test_build(self):
        table = HashTableSet()
        data = [Item(1, "sharry"), Item(3, "john"), Item(5, "harold")]
        table.build(data)
        assert table.find(3).value == "john"
