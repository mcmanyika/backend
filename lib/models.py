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


class t_images(models.Model):
    rootid = models.ForeignKey(Products, on_delete=models.CASCADE, default="1")
    img = models.ImageField(upload_to='product_images')
    status = models.CharField(max_length=10, default="active")
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def _str_(self):
        return self.status


class contact_supplier(models.Model):
    rootid = models.ForeignKey(Products, on_delete=models.CASCADE, default="1")
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=800)
    quantity = models.IntegerField()
    client = models.CharField(
        max_length=80, default='')
    owner = models.CharField(
        max_length=80, default='')
    status = models.CharField(max_length=10, default="active")
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def _str_(self):
        return self.title


class Urls(models.Model):
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    status = models.CharField(max_length=10, default='active')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def _str_(self):
        return self.name


class t_dict(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    status = models.CharField(max_length=10, default='active')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def _str_(self):
        return self.name


class Categories(models.Model):
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=100)
    status = models.CharField(max_length=10, default='active')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def _str_(self):
        return self.name


class SubCategories(models.Model):
    rootid = models.ForeignKey(
        Categories, on_delete=models.CASCADE, default="1")
    name = models.CharField(max_length=50)
    status = models.CharField(max_length=10, default='active')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def _str_(self):
        return self.name


class SecondSubCategories(models.Model):
    rootid = models.ForeignKey(
        SubCategories, on_delete=models.CASCADE, default="1")
    name = models.CharField(max_length=50)
    status = models.CharField(max_length=10, default='active')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def _str_(self):
        return self.name


class account_profile(models.Model):
    fname = models.CharField(max_length=50, default='')
    lname = models.CharField(max_length=50, default='')
    mobile = models.CharField(max_length=25, default='')
    email = models.EmailField(default='')
    owner = models.CharField(
        max_length=80, default='')
    verify = models.CharField(max_length=20, default="")
    status = models.CharField(max_length=10, default="active")
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def _str_(self):
        return self.fname


class t_business_info(models.Model):
    rootid = models.ForeignKey(
        account_profile, on_delete=models.CASCADE, default="")
    companyName = models.CharField(max_length=50, default="")
    address1 = models.CharField(max_length=50, default="")
    address2 = models.CharField(max_length=50, default="")
    postalCode = models.IntegerField()
    city = models.CharField(max_length=30, default="")
    country = models.CharField(max_length=50, default="Zimbabwe")
    companyOwner = models.CharField(max_length=50, default="")
    dob = models.CharField(max_length=10, default="")
    idType = models.CharField(max_length=20, default="")
    idCard = models.ImageField(upload_to='business_docs')
    numberOfEmployees = models.CharField(max_length=50, default="")
    registrationNumber = models.CharField(max_length=20, default="")
    regCertificate = models.ImageField(upload_to='business_docs')
    status = models.CharField(max_length=10, default="active")
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def _str_(self):
        return self.companyName
