class CategoryIterator:
    """Класс итератор для класса Category"""

    def __init__(self, category_obj):
        """Метод для итератора. Принимает объект класса Category."""
        self.category = category_obj
        self.index = 0

    def __iter__(self):
        """Метод для создания итератора."""
        self.index = 0
        return self

    def __next__(self):
        """Метод принимающий итератор."""
        if self.index < len(self.category.products_in_list):
            product = self.category.products_in_list[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration
