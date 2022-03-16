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


@api_view(['GET', 'POST'])
def url_list(request):
    if request.method == 'GET':
        data = Urls.objects.all()

        serializer = UrlSerializer(
            data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UrlSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def dict_list(request):
    if request.method == 'GET':
        data = t_dict.objects.all()

        serializer = DictSerializer(
            data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DictSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def category_list(request):
    if request.method == 'GET':
        data = Categories.objects.all()

        serializer = CategorySerializer(
            data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def subcategory_list(request):
    if request.method == 'GET':
        data = SubCategories.objects.all()

        serializer = SubCategorySerializer(
            data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SubCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def second_subcategory(request):
    if request.method == 'GET':
        data = SecondSubCategories.objects.all()

        serializer = SecondSubCategorySerializer(
            data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SecondSubCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
def acct_profile(request):
    if request.method == 'GET':
        data = account_profile.objects.all()

        serializer = ProfileSerializer(
            data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = account_profile.objects.all().order_by('-id')
    serializer_class = ProfileSerializer
