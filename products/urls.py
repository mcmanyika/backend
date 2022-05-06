from django.urls import path, include
from rest_framework import routers
from . import views
from .views import ProductViewSet

router = routers.DefaultRouter()
router.register(r'listing', ProductViewSet)
urlpatterns = [
    path('update/', include(router.urls)),
    path('products/', views.product_list, name='product_list'),
    path('images/', views.images, name='images'),
    path('imagesList/', views.ImageView.as_view(), name='images_list'),
    path('feedback/', views.feedback, name='feedback'),
    path('contact_supplier/', views.supplier_contact, name='contact_supplier'),
]
 