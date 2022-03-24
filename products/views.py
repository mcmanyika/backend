from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework import status
from rest_framework.views import APIView

from .models import *
from .serializers import *


@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        data = Products.objects.all()

        serializer = ProductSerializer(
            data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def feedback(request):
    if request.method == 'GET':
        data = Feedback.objects.all()

        serializer = FeedBackSerializer(
            data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FeedBackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "POST"])
def images(request):
    if request.method == "GET":
        data = t_images.objects.all()

        serializer = ImagesSerializer(
            data, context={"request": request}, many=True)

        return Response(serializer.data)

    elif request.method == "POST":
        serializer = ImagesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ImageView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, *args, **kwargs):
        imageList = t_images.objects.all()
        serializer = ImagesSerializer(imageList, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        imageList_serializer = ImagesSerializer(data=request.data)
        if imageList_serializer.is_valid():
            imageList_serializer.save()
            return Response(imageList_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', imageList_serializer.errors)
            return Response(imageList_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def supplier_contact(request):
    if request.method == 'GET':
        data = contact_supplier.objects.all()

        serializer = ContactSerializer(
            data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
