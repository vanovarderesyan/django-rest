from django.contrib.auth.models import User, Group
from .models import (   
            Items,
            Brands,
            Categories,
            Country,
            Dispatcher,
            ItemsImage,
            ItemVariant
            )
from rest_framework import serializers


class ItemsImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ItemsImage
        fields = ('url', 'item', 'item_id','image')

class BrandsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Brands
        fields = ('url', 'name', 'description', 'logo')

class CategoriesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categories
        fields = ('url', 'name', 'description', 'picture')


class CountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Country
        fields = ('url', 'name', 'code', 'continent_name')


class DispatcherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dispatcher
        fields = ('url', 'login', 'email','password')



class ItemVariantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ItemVariant
        fields = ('url', 'item', 'name', 'color','size','price','vendor')


class ItemsSerializer(serializers.HyperlinkedModelSerializer):
    images = ItemsImageSerializer(source='taskimage_set', many=True, read_only=True)
    image = ItemsImageSerializer(many=True, read_only=True)
    product_variant = ItemVariantSerializer(many=True, read_only=True)
    brand_name = serializers.CharField(source='brands.name', read_only=True)
    categories_name = serializers.CharField(source='category.name', read_only=True)
    country_name = serializers.CharField(source='country_of_origin.name', read_only=True)

    class Meta:
        model = Items
        fields = ('url', 'name', 'description', 'brands_id','vender_code','manufacturer_code','country_of_origin','season','brands','category','images','image','product_variant','brand_name','categories_name','country_name')

    def create(self, validated_data):
        images_data = self.context.get('view').request.FILES
        item = Items.objects.create(
                name=validated_data.get('name', 'no-name'),
                brands = validated_data.get('brands'),
                category = validated_data.get('category'),
                description = validated_data.get('description'),
                vender_code = validated_data.get('vender_code'),
                country_of_origin = validated_data.get('country_of_origin'),
                season = validated_data.get('season'),
                manufacturer_code = validated_data.get('manufacturer_code'),
                )
        for image_data in images_data.values():
            ItemsImage.objects.create(item=item, image=image_data)
        return item
