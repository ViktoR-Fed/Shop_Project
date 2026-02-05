from src.product import Product


class Smartphone(Product):
    """Дочерний класс представляющий смартфон"""

    efficiency: int
    model: str
    memory: int
    color: str

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        """Метод для получения общей суммы двух элементов (цена * количество)."""
        if type(other) is Smartphone:
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError
