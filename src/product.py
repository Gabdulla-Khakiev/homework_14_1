from typing import Dict


class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_data: Dict, products: list):
        for product in products:
            if product.name == product_data.get("name"):
                product.quantity += product_data.get("quantity")
                product.price = max(product.price, product_data.get("price"))
                return product

        new_product = cls(
            name=product_data.get("name"),
            description=product_data.get("description"),
            price=product_data.get("price"),
            quantity=product_data.get("quantity")
        )
        products.append(new_product)
        return new_product

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price: float):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif new_price < self.__price:
            confirm = input(f"Вы уверены, что хотите понизить цену с {self.__price} до {new_price}? (y/n): ").lower()
            if confirm == "y":
                self.__price = new_price
                print(f"Цена изменена на {new_price}")
            else:
                print("Действие отменено. Цена осталась прежней.")
        else:
            self.__price = new_price
            print(f"Цена изменена на {new_price}")
