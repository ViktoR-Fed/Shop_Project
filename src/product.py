class Product:
    """Класс представляющий продукт"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        """Метод для отображения информации по классу."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Метод для получения общей суммы двух элементов (цена * количество)."""
        if type(other) is Product:
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError

    @classmethod
    def new_product(cls, new_product: dict):
        """Метод, который принимает на вход параметры товара и возвращает созданный объект класса"""
        name, description, price, quantity = new_product.values()
        return cls(name, description, price, quantity)

    @property
    def price(self):
        """Геттер для получения приватного атрибута 'цена'"""
        return self.__price

    @price.setter
    def price(self, new_price: float):
        """Сеттер для присваивания нового значения приватного атрибута 'цена'"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

            # Если новая цена ниже текущей, запрашиваем подтверждение
        if new_price < self.__price:
            user_input = (
                input("Цена продукта ниже: Введите 'y' для подтверждения, 'n' для отмены!!!\n").strip().lower()
            )
            if user_input != "y":
                return  # отмена изменений

        self.__price = new_price
