from rest_framework import viewsets, permissions
from ecommerce.inventory.models import Product
from ecommerce.drf.serializer import AllProducts


class AllProductsViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()[:10]
    serializer_class = AllProducts
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
