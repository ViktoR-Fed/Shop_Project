import pytest

from src.category_iterator import CategoryIterator


def test_category_iterator(category_iterator):
    iter(category_iterator)
    assert category_iterator.index == 0
    assert next(category_iterator).name == "Samsung Galaxy S23 Ultra"
    assert next(category_iterator).name == "Iphone 15"
    assert next(category_iterator).name == "Xiaomi Redmi Note 11"

    with pytest.raises(StopIteration):
        next(category_iterator)
