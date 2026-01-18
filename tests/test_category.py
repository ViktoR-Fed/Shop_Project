import pytest

from src.category import Category
from src.product import Product


def test_category_initialization(sample_category):
    """Тест инициализации категории"""
    assert sample_category.name == "Смартфоны"
    assert "коммуникации" in sample_category.description
    assert len(sample_category.products_in_list) == 3


def test_category_products_list(sample_category, sample_products):
    """Тест списка продуктов в категории"""
    assert sample_category.products_in_list == sample_products
    assert len(sample_category.products_in_list) == 3

    for product in sample_category.products_in_list:
        assert isinstance(product, type(sample_products[0]))


def test_category_counter(sample_category):
    """Тест счетчика категорий"""
    assert Category.category_count >= 1
    assert Category.product_count >= len(sample_category.products_in_list)


def test_empty_category(sample_empty_category):
    """Тест пустой категории"""
    assert sample_empty_category.name == "Empty Category"
    assert sample_empty_category.description == "No products here"
    assert len(sample_empty_category.products_in_list) == 0


def test_multiple_categories():
    """Тест создания нескольких категорий"""
    # Сбрасываем счетчики для чистого теста
    Category.category_count = 0
    Category.product_count = 0

    # Создаем первую категорию
    products1 = [Product("Product 1", "Desc 1", 100.0, 1), Product("Product 2", "Desc 2", 200.0, 2)]
    category1 = Category("Category 1", "Description 1", products1)

    # Создаем вторую категорию
    products2 = [Product("Product 3", "Desc 3", 300.0, 3)]
    category2 = Category("Category 2", "Description 2", products2)

    assert Category.category_count == 2
    assert Category.product_count == 3
    assert len(category1.products_in_list) == 2
    assert len(category2.products_in_list) == 1


def test_category_attributes(sample_category):
    """Тест атрибутов категории"""
    assert hasattr(sample_category, "name")
    assert hasattr(sample_category, "description")
    assert hasattr(sample_category, "products")
    assert hasattr(Category, "category_count")
    assert hasattr(Category, "product_count")


def test_category_setter(sample_category, sample_product):
    assert len(sample_category.products_in_list) == 3
    sample_category.add_product(sample_product)
    assert len(sample_category.products_in_list) == 4
