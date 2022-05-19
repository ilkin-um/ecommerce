import pytest
from ecommerce.inventory import models

@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id,name,slug,is_active",
    [
        (1,"fashion","fashion",True),
        (2,"football","football",True),
        (3,"mma","mma",True),

    ],    
)
def test_inventory_category_dbfixture(
    db,db_fixture_setup,id,name,slug,is_active
):
    """
    Test category table against test data
    """
    result = models.Category.objects.get(id=id)
    assert result.name == name
    assert result.slug == slug
    assert result.is_active == is_active



@pytest.mark.parametrize(
    "name,slug,is_active",
    [
        ("fashion","fashion",True),
        ("football","football",True),
        ("mma","mma",True),

    ],    
)