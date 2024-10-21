class ZeroQuantityError(Exception):
    """Исключение для обработки добавления товаров с нулевым количеством"""

    def __init__(self, message="Товар с нулевым количеством не может быть добавлен."):
        self.message = message
        super().__init__(self.message)
