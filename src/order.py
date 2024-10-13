from src.base_category import BaseCategory
from src.product import Product


class Order(BaseCategory):
    def __init__(self, product: Product, quantity: int):
        super().__init__(name=product.name, description=product.description)
        self.product = product
        self.quantity = quantity
        self.total_price = self.calculate_total_price()

    def calculate_total_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return (f"Заказ: {self.product.name}, Количество: {self.quantity}, "
                f"Итоговая стоимость: {self.total_price} руб.")
