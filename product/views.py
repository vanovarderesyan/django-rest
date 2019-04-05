from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import (
        ItemsSerializer,
        ItemVariantSerializer,
        BrandsSerializer,
        ItemsImageSerializer,
        CategoriesSerializer,
        CountrySerializer,
        DispatcherSerializer
        )
from .models import (
            Items,
            Brands,
            ItemsImage,
            ItemVariant,
            Categories,
            Country,
            Dispatcher
        )


class ItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer




class BrandsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Brands.objects.all()
    serializer_class = BrandsSerializer

class ItemsImageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ItemsImage.objects.all()
    serializer_class = ItemsImageSerializer


class ItemVariantViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ItemVariant.objects.all()
    serializer_class = ItemVariantSerializer


class CategoriesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer

class CountryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class DispatcherViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Dispatcher.objects.all()
    serializer_class = DispatcherSerializer




