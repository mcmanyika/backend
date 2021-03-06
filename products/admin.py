from django.contrib import admin
from .models import *


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'moq', 'status')


admin.site.register(Products, ProductsAdmin)


class ImagesAdmin(admin.ModelAdmin):
    list_display = ("rootid", "status")


admin.site.register(t_images, ImagesAdmin)


class FeedBackAdmin(admin.ModelAdmin):
    list_display = ('id','rootid', 'rate',  'status')


admin.site.register(Feedback, FeedBackAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','rootid', 'title', 'quantity',  'status')


admin.site.register(contact_supplier, ContactAdmin)
