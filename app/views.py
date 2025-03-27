from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Category, Photo, About


def home(request):
    categories = Category.objects.all()
    photos = Photo.objects.all()
    context = {"categories": categories, "photos": photos}
    return render(request, "index.html", context)


def add_photo(request):
    user = request.user

    categories = Category.objects.all()

    if request.method == "POST":
        data = request.POST
        images = request.FILES.getlist("images")

        if data["category"] != "none":
            category = Category.objects.get(id=data["category"])
        elif data["category_new"] != "":
            category, created = Category.objects.get_or_create(
                user=user, name=data["category_new"]
            )
        else:
            category = None

        for image in images:
            photo = Photo.objects.create(
                category=category,
                description=data["description"],
                image=image,
            )

            return redirect("home")
        context = {"categories": categories, "photo": photo}
        return render(request, "add.html", context)
    # , "categories": categories

    #  title = request.POST.get("title")
    #     description = request.POST.get("description")
    #     image = request.FILES.get_list("image")
    #     category_id = request.POST.get("category")
    #     category = Category.objects.get(id=category_id)

    #     photo = Photo.objects.create(
    #         title=title,
    #         description=description,
    #         image=image,
    #         category=category,
    #         user=user,
    #     )


def detailed_view(request, pk):
    photos = Photo.objects.get(id=pk)
    context = {"photos": photos}
    return render(request, "detailed.html", context)


def about(request):
    return render(request, "about.html")
