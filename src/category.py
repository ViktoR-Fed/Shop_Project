from src.product import Product


class Category:
    """Класс представляющий категорию продукта"""

    name: str
    description: str
    products: list[Product]
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        """Метод ждя инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: Product):
        """Метод для добавления продуктов"""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        """Геттер, для вывода списка товаров в виде строки"""
        product_str = ""
        for product in self.__products:
            product_str = f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return product_str

    @property
    def products_in_list(self):
        return self.__products
