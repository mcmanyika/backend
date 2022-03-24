from rest_framework import serializers
from .models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('id', 'title', 'description', 'price',
                  'image', 'moq', 'availability', 'measurementType', 'category', 'owner', 'status')


class FeedBackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = t_images
        fields = ("rootid", "img", "status")


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = contact_supplier
        fields = ("rootid", "title", 'description',
                  'quantity', 'client', 'owner', "status")
