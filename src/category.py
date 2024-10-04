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

    @property
    def products(self):
        product_str = ''
        for product in self.__products:
            product_str += f'{product.name}, {product.price}. Остаток: {product.quantity}.'
        return product_str

    @products.setter
    def add_product(self, product: Product):
        self.__products.append(product)
        Category.total_products += 1
