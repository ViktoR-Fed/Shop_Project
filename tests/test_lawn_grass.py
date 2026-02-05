import pytest


def test_lawn_grass_init(lawn_grass_product1):
    assert lawn_grass_product1.name == "Газонная трава"
    assert lawn_grass_product1.description == "Элитная трава для газона"
    assert lawn_grass_product1.price == 500.0
    assert lawn_grass_product1.quantity == 20
    assert lawn_grass_product1.country == "Россия"
    assert lawn_grass_product1.germination_period == "7 дней"
    assert lawn_grass_product1.color == "Зеленый"


def test_lawn_grass_add(lawn_grass_product1, lawn_grass_product2):
    assert lawn_grass_product1 + lawn_grass_product2 == 16750.0


def test_lawn_grass_add_error(lawn_grass_product1):
    with pytest.raises(TypeError):
        result = lawn_grass_product1 + 1
