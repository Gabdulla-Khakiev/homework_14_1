from src.category import Category
from src.product import Product


class CategoryIterator:

    def __init__(self, category_obj: Category):
        self.category = category_obj
        self.index = 0

    def __iter__(self, category):
        return self

    def __next__(self):
        if self.index < len(self.category.products):
            product = self.category.products[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration
