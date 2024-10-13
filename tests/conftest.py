import pytest

from src.category_iterator import CategoryIterator
from src.category import Category
from src.product import Product
from src.order import Order


@pytest.fixture
def product1():
    return Product(name="Iphone 15", description="512GB, Gray space", price=210000.0, quantity=8)


@pytest.fixture
def product2():
    return Product(name="Samsung Galaxy C23 Ultra", description="256GB, Серый цвет, 200MP камера", price=180000.0,
                   quantity=5)


@pytest.fixture
def category_for_iterator():
    return Category(
        name="Смартфоны",
        description="Смартфоны для всех",
        products=[
            Product(name="Iphone 15", description="512GB, Gray space", price=210000.0, quantity=8),
            Product(name="Samsung Galaxy C23 Ultra", description="256GB, Серый цвет, 200MP камера", price=180000.0,
                    quantity=5)
        ]
    )


@pytest.fixture
def category_iterator(category_for_iterator):
    iterator = CategoryIterator(category_for_iterator)
    return iterator


product_for_order = Product(name="Iphone 15", description="512GB, Gray space", price=210000.0, quantity=8)


@pytest.fixture
def order():
    order = Order(product_for_order, 5)
    return order
