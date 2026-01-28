import pytest

from src.category import Category
from src.category_iterator import CategoryIterator
from src.lawn_grass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


@pytest.fixture
def sample_products():
    """Фикстура для создания тестовых продуктов"""
    return [
        Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
        Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
        Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14),
    ]


@pytest.fixture
def sample_category(sample_products):
    """Фикстура для создания тестовой категории"""
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        sample_products,
    )


@pytest.fixture
def sample_product():
    """Фикстура для создания одиночного продукта"""
    return Product("Test Product", "Test Description", 1000.0, 10)


@pytest.fixture
def sample_empty_category():
    """Фикстура для создания пустой категории"""
    return Category("Empty Category", "No products here", [])


@pytest.fixture(autouse=True)
def reset_category_counters():
    """Фикстура для сброса счетчиков перед каждым тестом"""
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture
def category_iterator(sample_category):
    return CategoryIterator(sample_category)


@pytest.fixture
def smartphone_product1():
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )


@pytest.fixture
def smartphone_product2():
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")


@pytest.fixture
def lawn_grass_product1():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def lawn_grass_product2():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
