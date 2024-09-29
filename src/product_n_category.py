import json


class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    name: str
    description: str
    products: list[Product]
    total_categories = 0
    total_products = 0

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.products = []

        Category.total_categories += 1

    def add_product(self, product: Product):
        self.products.append(product)
        Category.total_products += 1


def read_json_file():
    """Загружает данные категорий и продуктов из JSON файла."""
    with open('data/products.json','r', encoding='utf8') as file:
        products = json.load(file)

    categories = []

    for category_data in products:
        category = Category(name=category_data['name'], description=category_data['description'])

        for product_data in category_data['products']:
            product = Product(
                name=product_data['name'],
                description=product_data['description'],
                price=product_data['price'],
                quantity=product_data['quantity']
            )
            category.add_product(product)

        categories.append(category)

    return categories


if __name__ == "__main__":
    categories = read_json_file()

    # Вывод информации о категориях и продуктах
    for category in categories:
        print(f"Category: {category.name}, Description: {category.description}")
        for product in category.products:
            print(f"  Product: {product.name}, Price: {product.price}, Quantity: {product.quantity}")

    # Вывод общего количества категорий и товаров
    print(f"Total Categories: {Category.total_categories}, Total Products: {Category.total_products}")
