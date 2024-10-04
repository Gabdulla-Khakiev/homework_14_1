import pytest


from src.product import Product
from src.category import Category


def test_product_initialization():
    product = Product(name="Samsung Galaxy C23 Ultra", description="256GB, Серый цвет, 200MP камера", price=180000.0,
                      quantity=5)

    assert product.name == "Samsung Galaxy C23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_product_count():
    prod_list = []
    category = Category(name="Смартфоны", description="Смартфоны, как средство не только коммуникации", products=prod_list)
    assert Category.total_products == 0


if __name__ == "__main__":
    pytest.main()
