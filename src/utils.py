import json
import os

from src.category import Category
from src.product import Product


def read_json(path: str) -> dict:
    """Функция для чтения JSON-файла"""
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="UTF-8") as file:
        data = json.load(file)
    return data


def create_objects_from_json(data):
    """Функция для создания объектов из полученных данных"""
    categories = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))
    return categories
