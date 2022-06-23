from django.shortcuts import get_object_or_404
from ecommerce.drf.serializer import ProductInventorySerializer
from ecommerce.inventory.models import Product, ProductInventory
from rest_framework import mixins, permissions, viewsets
from rest_framework.response import Response


class ProductByCategory(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
):
    """
    API endpoint that returns products by category
    """

    queryset = ProductInventory.objects.all()

    def list(self, request, slug=None):
        queryset = ProductInventory.objects.filter(
            product__category__slug=slug,
        ).filter(is_default=True)[:10]
        serializer = ProductInventorySerializer(
            queryset, context={"request": request}, many=True
        )
        return Response(serializer.data)
