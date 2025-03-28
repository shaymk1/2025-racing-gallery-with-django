from django.shortcuts import render, redirect
from .models import Category, Photo, About


def home(request):
    category = request.GET.get("category")  # get the category from the request
    if category is None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name=category)
    categories = Category.objects.all()

    context = {
        "categories": categories,
        "photos": photos,
        "category": category,
    }
    return render(request, "index.html", context)


def detailed_view(request, pk):
    photos = Photo.objects.get(id=pk)
    context = {"photos": photos}
    return render(request, "detailed.html", context)


def add_photo(request):
    categories = Category.objects.all()

    if request.method == "POST":
        data = request.POST
        images = request.FILES.get("images")
        if data["category"] != "none":
            category = Category.objects.get(id=data["category"])
        elif data["category_new"] != "":
            category, created = Category.objects.get_or_create(
                name=data["category_new"]
            )
        else:
            category = None
        photo = Photo.objects.create(
            category=category,
            description=data["description"],
            pic=images,
        )
        return redirect("home")
    context = {"categories": categories}

    return render(request, "add_photo.html", context)


def delete_photo(request, pk):
    photo = Photo.objects.get(id=pk)
    if request.method == "POST":
        photo.delete()
        return redirect("home")
    context = {"photos": photo}
    return render(request, "delete_photo.html", context)


# def edit_photo(request, pk):
#     categories = Category.objects.all()
#     photo = Photo.objects.get(id=pk)
#     if request.method == "POST":
#         data = request.POST
#         images = request.FILES.get("images")
#         if data["category"] != "none":
#             category = Category.objects.get(id=data["category"])
#         elif data["category_new"] != "":
#             category, created = Category.objects.get_or_create(
#                 name=data["category_new"]
#             )
#         else:
#             category = None
#         photo.category = category
#         photo.description = data["description"]
#         if images:
#             photo.pic = images
#         photo.save()
#         return redirect("home")


def about(request):
    return render(request, "about.html")


def search(request):
    query = request.GET.get("q")  # Get the search query from the URL
    posts = (
        Photo.objects.filter(title__icontains=query) if query else []
    )  # Filter results
    return render(request, "search.html", {"query": query, "posts": posts})
