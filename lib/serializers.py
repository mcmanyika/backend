from rest_framework import serializers
from .models import *


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


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = account_profile
        fields = '__all__'


class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = t_business_info
        fields = '__all__'
