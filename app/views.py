from django.shortcuts import render


def home(request):
    return render(request, "index.html")


def add_photo(request):
    return render(request, "add.html")


def detailed_view(request, pk):
    return render(request, "detailed.html")


def about(request):
    return render(request, "about.html")
