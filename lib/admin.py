from django.contrib import admin
from .models import *


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


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('fname', 'lname', 'email',  'status')


admin.site.register(account_profile, ProfileAdmin)


class BusinessAdmin(admin.ModelAdmin):
    list_display = ('companyName', 'city', 'country',  'status')


admin.site.register(t_business_info, BusinessAdmin)
