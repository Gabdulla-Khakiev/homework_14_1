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


def test_category_str():
    category_empty = Category(name="Смартфоны", description="Смартфоны для всех")
    assert str(category_empty) == "Смартфоны, количество продуктов: 0 шт."

    product1 = Product(name="Iphone 15", description="512GB, Gray space", price=210000.0, quantity=8)
    product2 = Product(name="Samsung Galaxy C23 Ultra", description="256GB, Серый цвет, 200MP камера", price=180000.0, quantity=5)

    category_with_products = Category(name="Смартфоны", description="Смартфоны для всех", products=[product1, product2])
    assert str(category_with_products) == "Смартфоны, количество продуктов: 2 шт."


if __name__ == "__main__":
    pytest.main()
