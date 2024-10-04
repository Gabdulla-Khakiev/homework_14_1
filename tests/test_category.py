import pytest

from src.category import Category
from src.product import Product


def test_category_initialization():
    # Проверка корректности инициализации объекта Category
    category = Category(name="Смартфоны", description="Смартфоны для всех")
    assert category.name == "Смартфоны"
    assert category.description == "Смартфоны для всех"
    assert Category.total_categories == 1


def test_category_count():
    Category.total_categories = 0
    category1 = Category(name="Смартфоны", description="Смартфоны, как средство не только коммуникации")
    category2 = Category(name="Телевизоры", description="Современные телевизоры для удобного просмотра")

    assert Category.total_categories == 2


def test_add_product():
    # Проверка добавления продукта в категорию
    category = Category(name="Смартфоны", description="Смартфоны для всех")
    product = Product(name="Iphone 15", description="512GB, Gray space", price=210000.0, quantity=8)
    category.add_product(product)

    assert category.products == "Iphone 15, 210000.0 руб. Остаток: 8 шт."


if __name__ == "__main__":
    pytest.main()
