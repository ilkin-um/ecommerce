import django
import py
import pytest


@pytest.fixture
def create_super_user(django_user_model):

    return django_user_model.objects.create_superuser("admin","","admin")