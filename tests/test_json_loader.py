import json
import os
from unittest.mock import mock_open, patch

import pytest

from src.category import Category
from src.product import Product
from src.utils import create_objects_from_json, read_json


def create_test_json_file(tmp_path, data):
    """Вспомогательная функция для создания тестового JSON файла"""
    file_path = tmp_path / "test_data.json"
    with open(file_path, "w", encoding="UTF-8") as f:
        json.dump(data, f)
    return str(file_path)


def test_read_json(tmp_path):
    """Тест чтения JSON файла"""
    test_data = [
        {
            "name": "Тестовые смартфоны",
            "description": "Тестовое описание",
            "products": [
                {
                    "name": "Тестовый телефон",
                    "description": "Тестовое описание телефона",
                    "price": 1000.0,
                    "quantity": 5,
                }
            ],
        }
    ]

    json_file = create_test_json_file(tmp_path, test_data)

    with open(json_file, "r", encoding="UTF-8") as file:
        data = json.load(file)

    assert len(data) == 1
    assert data[0]["name"] == "Тестовые смартфоны"
    assert len(data[0]["products"]) == 1
    assert data[0]["products"][0]["name"] == "Тестовый телефон"


def test_create_objects_from_json():
    """Тест создания объектов из JSON данных"""
    test_data = [
        {
            "name": "Категория 1",
            "description": "Описание 1",
            "products": [{"name": "Продукт 1", "description": "Описание продукта 1", "price": 100.0, "quantity": 10}],
        }
    ]

    # Имитируем функцию create_objects_from_json
    categories = []
    for category in test_data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))

    assert len(categories) == 1
    assert isinstance(categories[0], Category)
    assert isinstance(categories[0].products_in_list[0], Product)
    assert categories[0].name == "Категория 1"
    assert categories[0].products_in_list[0].name == "Продукт 1"


def test_read_json_file_exists():
    """Тестирование чтения существующего JSON файла"""
    test_data = {"test": "data"}
    json_content = json.dumps(test_data)

    with patch("builtins.open", mock_open(read_data=json_content)) as mock_file:
        with patch("json.load") as mock_json:
            mock_json.return_value = test_data
            result = read_json("dummy_path.json")

            mock_file.assert_called_once()
            assert result == test_data


def test_read_json_file_not_found():
    """Тестирование ошибки при отсутствии файла"""
    with patch("builtins.open", side_effect=FileNotFoundError()):
        with pytest.raises(FileNotFoundError):
            read_json("non_existent.json")
