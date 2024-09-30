class Category:
    name: str
    description: str
    products: list
    total_categories = 0
    total_products = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.products = products if products else []

        Category.total_categories += 1
        Category.total_products += len(products) if products else 0