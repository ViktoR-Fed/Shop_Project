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


def test_product_zero_quantity():
    """Тест продукта с нулевым количеством"""
    product = Product("Zero Product", "No items", 500.0, 0)
    assert product.quantity == 0
    assert product.name == "Zero Product"
