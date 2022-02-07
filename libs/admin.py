from django.contrib import admin
from .models import *


class AcctAttributesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sponser', 'status')


admin.site.register(AcctAttributes, AcctAttributesAdmin)


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'moq', 'status')


admin.site.register(Products, ProductsAdmin)


class ImagesAdmin(admin.ModelAdmin):
    list_display = ("rootid", "status")


admin.site.register(t_images, ImagesAdmin)


class UrlsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'status')


admin.site.register(Urls, UrlsAdmin)


class DictAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'status')


admin.site.register(t_dict, DictAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',  'status')


admin.site.register(Categories, CategoryAdmin)


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'rootid', 'name',  'status')


admin.site.register(SubCategories, SubCategoryAdmin)


class SecondSubCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'rootid', 'name',  'status')


admin.site.register(SecondSubCategories, SecondSubCategoryAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('rootid', 'title', 'quantity',  'status')


admin.site.register(contact_supplier, ContactAdmin)
