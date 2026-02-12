from itertools import product
from unittest.mock import patch

import pytest

from src.product import Product


def test_product_initialization(sample_product):
    """Тест инициализации продукта"""
    assert sample_product.name == "Test Product"
    assert sample_product.description == "Test Description"
    assert sample_product.price == 1000.0
    assert sample_product.quantity == 10


def test_product_attribute_types(sample_product):
    """Тест типов атрибутов продукта"""
    assert isinstance(sample_product.name, str)
    assert isinstance(sample_product.description, str)
    assert isinstance(sample_product.price, float)
    assert isinstance(sample_product.quantity, int)


def test_multiple_products(sample_products):
    """Тест создания нескольких продуктов"""
    assert len(sample_products) == 3

    product1, product2, product3 = sample_products

    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.price == 180000.0

    assert product2.name == "Iphone 15"
    assert product2.price == 210000.0

    assert product3.name == "Xiaomi Redmi Note 11"
    assert product3.price == 31000.0


def test_new_product(sample_product):
    product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.quantity == 5
    assert product.price == 180000.0
    assert product.description == "256GB, Серый цвет, 200MP камера"


def test_setter_price(capsys, sample_product):
    sample_product.price = 0
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-1] == "Цена не должна быть нулевая или отрицательная"
    sample_product.price = 1800
    assert sample_product.price == 1800


def test_price_confirm_lower_with_yes(sample_product):
    with patch("builtins.input", return_value="y"):
        sample_product.price = 5.0
    assert sample_product.price == 5.0


def test_str_category():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    assert (str(product1)) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
    assert (str(product2)) == "Iphone 15, 210000.0 руб. Остаток: 8 шт."
    assert (str(product3)) == "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."
