from django.db import models


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
    rootid = models.CharField(max_length=80, default="")
    companyName = models.CharField(max_length=50, default="")
    address1 = models.CharField(max_length=50, default="")
    address2 = models.CharField(max_length=50, default="")
    postalCode = models.IntegerField()
    city = models.CharField(max_length=30, default="")
    country = models.CharField(max_length=50, default="Zimbabwe")
    companyOwner = models.CharField(max_length=50, default="")
    dob = models.CharField(max_length=10, default="")
    # idType = models.CharField(max_length=20, default="")
    # idCard = models.ImageField(upload_to='business_docs')
    numberOfEmployees = models.CharField(max_length=50, default="")
    # registrationNumber = models.CharField(max_length=20, default="")
    # regCertificate = models.ImageField(upload_to='business_docs')
    status = models.CharField(max_length=10, default="active")
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def _str_(self):
        return self.companyName
