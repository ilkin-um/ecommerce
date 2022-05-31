from django.core import serializers
from django.shortcuts import render
from ecommerce.inventory import models


def home(request):

    return render(request, "index.html")


def category(request):

    data = models.Category.objects.all()

    return render(request, "categories.html", {"data": data})


def category(request):

    data = models.Category.objects.all()

    return render(request, "categories.html", {"data": data})


def product_by_category(request, category):

    y = models.Product.objects.filter(category__name=category).values(
        "id", "name", "slug", "created_at", "category__name", "product__store_price"
    )

    return render(request, "product_by_category.html", {"data": y})
