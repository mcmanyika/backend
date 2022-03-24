from django.db import models


class Products(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    image = models.ImageField(upload_to='product_images')
    moq = models.IntegerField()
    availability = models.CharField(max_length=20, default='Ready to ship')
    measurementType = models.CharField(max_length=20, default='Kilograms')
    owner = models.CharField(
        max_length=80, default='')
    status = models.CharField(max_length=10, default='active')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def _str_(self):
        return self.title


class Feedback(models.Model):
    rootid = models.ForeignKey(
        Products, on_delete=models.CASCADE, default="")
    description = models.TextField()
    rate = models.IntegerField()
    status = models.CharField(max_length=10, default='active')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def _str_(self):
        return self.rootid


class t_images(models.Model):
    rootid = models.ForeignKey(Products, on_delete=models.CASCADE, default="1")
    img = models.ImageField(upload_to='product_images')
    status = models.CharField(max_length=10, default="active")
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def _str_(self):
        return self.status
