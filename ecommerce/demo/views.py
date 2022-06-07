from django.shortcuts import render
from ecommerce.inventory import models
from django.db.models import Count
from django.contrib.postgres.aggregates import ArrayAgg


def home(request):

    return render(request, "index.html")


def category(request):

    data = models.Category.objects.all()

    return render(request, "categories.html", {"data": data})


def product_by_category(request, category):

    data = models.Product.objects.filter(category__name=category).values(
        "id", "name", "slug", "category__name", "product__store_price"
    )

    return render(request, "product_by_category.html", {"data": data})


def product_detail(request, slug):

    filter_args = []

    if request.GET:
        for value in request.GET.values():
            filter_args.append(value)

        x = (
            models.ProductInventory.objects.filter(product__slug=slug)
            .filter(attribute_values__attribute_value__in=filter_args)
            .annotate(num_tags=Count("attribute_values"))
            .filter(num_tags=len(filter_args))
            .values(
                "id", "sku", "product__name", "store_price", "product_inventory__units"
            )
            .annotate(field_a=ArrayAgg("attribute_values__attribute_value"))
            .get()
        )
    else:
        x = (
            models.ProductInventory.objects.filter(product__slug=slug)
            .filter(is_default=True)
            .values(
                "id", "sku", "product__name", "store_price", "product_inventory__units"
            )
            .annotate(field_a=ArrayAgg("attribute_values__attribute_value"))
            .get()
        )

    y = (
        models.ProductInventory.objects.filter(product__slug=slug)
        .distinct()
        .values(
            "attribute_values__product_attribute__name",
            "attribute_values__attribute_value",
        )
    )

    z = (
        models.ProductTypeAttribute.objects.filter(
            product_type__product_type__product__slug=slug
        )
        .distinct()
        .values("product_attribute__name")
    )

    return render(request, "product_detail.html", {"x": x, "filter": y, "z": z})
