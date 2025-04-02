from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.name


class Photo(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    pic = models.ImageField(upload_to="static", blank=False, null=False)
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.description


class About(models.Model):
    image = models.ImageField(upload_to="static/photos/", blank=False, null=False)
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.title