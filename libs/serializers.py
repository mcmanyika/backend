from rest_framework import serializers
from .models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('id', 'title', 'description', 'price',
                  'image', 'moq', 'availability', 'measurementType', 'category', 'owner', 'status')


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = t_images
        fields = ("rootid", "img", "status")


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = contact_supplier
        fields = ("rootid", "title", 'description',
                  'quantity', 'owner', "status")


class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Urls
        fields = ('id', 'name', 'icon', 'category', 'status')


class DictSerializer(serializers.ModelSerializer):
    class Meta:
        model = t_dict
        fields = ('id', 'name', 'category', 'status')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ('id', 'name', 'icon', 'status')


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategories
        fields = ('rootid', 'name', 'status')


class SecondSubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SecondSubCategories
        fields = ('rootid', 'name', 'status')
