
from django.shortcuts import render
from .models import Category, Photo


def home(request):
    categories = Category.objects.all()
    photos = Photo.objects.all()
    context = {"categories": categories, "photos": photos}
    return render(request, "index.html", context)


def add_photo(request):
    return render(request, "add.html")


def detailed_view(request, pk):
    photos = Photo.objects.get(id=pk)
    context = {"photos": photos}
    return render(request, "detailed.html", context)


def about(request):
    return render(request, "about.html")
