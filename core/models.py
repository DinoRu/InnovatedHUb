from django.db import models


class WorkCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()

    def __str__(self):
        return self.name


class TechTool(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Work(models.Model):
    category = models.ForeignKey(WorkCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    overview = models.CharField(max_length=300)
    thumbnail = models.ImageField(upload_to='Works/')
    description = models.TextField()
    created = models.DateField(auto_now_add=True)
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    usse_tech = models.ForeignKey(TechTool, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    logo = models.ImageField(upload_to='Clients/')
    slug = models.SlugField()
    about_firm = models.TextField()

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    messages = models.TextField()

    def __str__(self):
        return self.name
