from src.product import Product


class Category:
    name: str
    description: str
    products: list
    total_categories = 0
    total_products = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products else []

        Category.total_categories += 1
        Category.total_products += len(products) if products else 0

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    @property
    def products(self):
        product_str = ''
        for product in self.__products:
            product_str += f"{str(product)}\n"
        return product_str

    @property
    def products_list(self):
        return self.__products

    def add_product(self, product: Product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.total_products += 1
        else:
            raise TypeError
