from django.db.models.fields.related import ManyToManyField
from ecommerce.inventory.models import (
    Brand,
    Category,
    Media,
    Product,
    ProductAttributeValue,
    ProductInventory,
    ProductType,
)
from rest_framework import serializers


class ProductAttributeValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAttributeValue
        # fields = "__all__"
        depth = 2
        exclude = ["id"]


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ["name"]


class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = ["name"]


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ["alt_text"]
        read_only = True
        editable = False


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["name"]
        read_only = True
        editable = False


class ProductInventorySerializer(serializers.ModelSerializer):
    """
    product = ProductSerializer(many=False, read_only=True)
    image = MediaSerializer(source="media_product_inventory", many=True, read_only=True)
    type = ProductTypeSerializer(source="product_type", many=False, read_only=True)
    brand = BrandSerializer(many=False, read_only=True)
    attributes = ProductAttributeValueSerializer(
        source="attribute_values", many=True, read_only=True
    )
    price = serializers.DecimalField(
        source="retail_price", max_digits=5, decimal_places=2
    )
    """

    product = ProductSerializer(many=False, read_only=True)

    class Meta:
        model = ProductInventory
        fields = [
            "id",
            "sku",
            "store_price",
            "is_default",
            "product",
        ]
        read_only = True
