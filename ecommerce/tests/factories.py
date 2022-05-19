import factory
import pytest
from faker import Faker
from pytest_factoryboy import register
from ecommerce.inventory import models

fake_data = Faker()


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Category

    name = factory.Sequence(lambda n: "cat_slug_%d" % n)
    slug = fake_data.lexify(text="cat_slug_?????")
    is_active = fake_data.lexify(text="cat_slug_?????")


register(CategoryFactory)
