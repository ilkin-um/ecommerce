from math import prod
from psycopg2 import IntegrityError
import pytest
from ecommerce.inventory import models


"""
Category table tests
"""


@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id,name,slug,is_active",
    [
        (1, "fashion", "fashion", 1),
        (18, "trainers", "trainers", 1),
        (35, "baseball", "baseball", 1),
    ],
)
def test_inventory_category_dbfixture(db, db_fixture_setup, id, name, slug, is_active):
    """
    Test category table against test data
    """
    result = models.Category.objects.get(id=id)
    assert result.name == name
    assert result.slug == slug
    assert result.is_active == is_active


@pytest.mark.parametrize(
    "slug,is_active",
    [
        ("fashion", 1),
        ("trainers", 1),
        ("baseball", 1),
    ],
)
def test_inventory_db_category_insert(db, category_factory, slug, is_active):
    result = category_factory.create(slug=slug, is_active=is_active)
    print(result.name)
    assert result.slug == slug
    assert result.is_active == is_active


"""
Product table tests
"""


@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id,web_id,name,slug,description,is_active,created_at,updated_at",
    [
        (
            1,
            "45425812",
            "girl primotoo open toe synthetiflip flop sandal",
            "girl-primotoo-open-toe-synthetiflip-flop-sandal",
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin porta, eros vel sollicitudin lacinia, quam metus gravida elit, a elementum nisl neque sit amet orci. Nulla id lorem ac nunc cursus consequat vitae ut orci. In a velit eu justo eleifend tincidunt vel eu turpis. Praesent eu orci egestas, lobortis magna egestas, tincidunt augue. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Aenean vitae lectus eget tortor laoreet efficitur vel et leo. Maecenas volutpat eget ante id tempor. Etiam posuere ex urna, at aliquet risus tempor eu. Aenean a odio odio. Nunc consectetur lorem ante, interdum ultrices elit consectetur sit amet. Vestibulum rutrum interdum nulla. Cras vel mi a enim eleifend blandit. Curabitur ex dui, rutrum et odio sit amet, auctor euismod massa.",
            "1",
            "2021-09-04 22:14:18.279096",
            "2021-09-04 22:14:18.279096",
        ),
    ],
)
def test_inventory_db_product_dbfixture(
    db,
    db_fixture_setup,
    id,
    web_id,
    name,
    slug,
    description,
    is_active,
    created_at,
    updated_at,
):
    result = models.Product.objects.get(id=id)
    result_created_at = result.created_at.strftime("%Y-%m-%d %H:%M%:%S")

    assert result.web_id == web_id
    assert result.name == name
    assert result.slug == slug
    assert result_created_at == created_at


def test_inventory_db_product_is_unique(db, product_factory):
    new_id = 3312353
    new_web_id = product_factory.create(web_id=new_id)

    with pytest.raises(IntegrityError):
        product_factory.create(web_id=new_id)


@pytest.mark.dbfixture
def test_inventory_db_product_insert(db, product_factory, category_factory):
    new_category = category_factory.create()
    new_product = product_factory.create(category=(1, 18))
    num_of_product_categories = new_product.category.all().count()

    assert "web_id_" in new_product.web_id
    assert num_of_product_categories == 2
