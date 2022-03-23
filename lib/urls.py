from django.urls import path, include
from rest_framework import routers
from . import views
from .views import ProfileViewSet

router = routers.DefaultRouter()
router.register(r'profile', ProfileViewSet)
urlpatterns = [
    path('update/', include(router.urls)),
    path('products/', views.product_list, name='product_list'),
    path('images/', views.images, name='images'),
    path('urls/', views.url_list, name='url_list'),
    path('dict/', views.dict_list, name='dict_list'),
    path('categories/', views.category_list, name='category_list'),
    path('subcategories/', views.subcategory_list, name='subcategory_list'),
    path('second_subcategories/', views.second_subcategory,
         name='second_subcategories'),
    path('imagesList/', views.ImageView.as_view(), name='images_list'),
    path('contact_supplier/', views.supplier_contact, name='contact_supplier'),
    path('add_profile/', views.acct_profile, name='add_profile'),
    path('account_profile/', views.acct_profile, name='account_profile'),
    path('business-info/', views.business_info, name='business-info'),
    path('feedback/', views.feedback, name='feedback'),
]
