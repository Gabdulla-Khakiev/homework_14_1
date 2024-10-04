import pytest

from src.category import Category


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


if __name__ == "__main__":
    pytest.main()
