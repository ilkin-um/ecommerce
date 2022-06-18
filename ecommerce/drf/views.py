from rest_framework.response import Response
from rest_framework import viewsets, permissions, mixins
from ecommerce.inventory.models import Product
from ecommerce.drf.serializer import AllProducts


class AllProductsViewSet(
    viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin
):

    queryset = Product.objects.all()
    serializer_class = AllProducts
    lookup_field = "slug"
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def retrieve(self, request, slug=None):
        queryset = Product.objects.filter(category__slug=slug)[:10]
        serializer = AllProducts(queryset, many=True)

        return Response(serializer.data)
