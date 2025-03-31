from django.shortcuts import render, redirect
from .models import Category, Photo
from django.core.paginator import Paginator
from django.http import JsonResponse
from PIL import Image


# def home(request):
#     category = request.GET.get("category")  # get the category from the request
#     if category and category != "all":
#         photos = Photo.objects.filter(category__name=category)
#     else:
#         photos = Photo.objects.all()
#     categories = Category.objects.all()

#     # Pagination
#     paginator = Paginator(photos, 6)  # Show 6 photos per page
#     page_number = request.GET.get("page", 1)
#     page_obj = paginator.get_page(page_number)

#     # Check if it's an AJAX request
#     if request.headers.get("x-requested-with") == "XMLHttpRequest":
#         photos_data = [
#             {
#                 "id": photo.id,
#                 "pic_url": photo.pic.url,
#                 "title": photo.title,
#                 "category": photo.category.name if photo.category else "Uncategorized",
#                 "description": photo.description,
#             }
#             for photo in page_obj
#         ]
#         return JsonResponse({"photos": photos_data, "has_next": page_obj.has_next()})

#     context = {
#         "categories": categories,
#         "photos": page_obj,
#         "category": category,
#     }

#     return render(request, "index.html", context)


#


def home(request):
    category = request.GET.get("category")  # Get the category filter from the request
    if category and category != "all":
        photos = Photo.objects.filter(category__name=category)
    else:
        photos = Photo.objects.all()

    categories = Category.objects.all()

    # Paginate the photos
    paginator = Paginator(photos, 6)  # Show 6 photos per page
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)

    if (
        request.headers.get("x-requested-with") == "XMLHttpRequest"
    ):  # Check if it's an AJAX request
        photos_data = [
            {
                "id": photo.id,
                "pic_url": photo.pic.url,
                "title": photo.title,
                "category": photo.category.name if photo.category else "Uncategorized",
                "description": photo.description,
            }
            for photo in page_obj
        ]
        return JsonResponse({"photos": photos_data, "has_next": page_obj.has_next()})

    context = {
        "categories": categories,
        "photos": page_obj,
        "category": category,  # Pass the selected category to the template
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
            # save the Photo object
        photo = Photo.objects.create(
            category=category,
            title=data["title"],
            description=data["description"],
            pic=images,
        )
        # Resize the image using PIL
      
        if images:
            img = Image.open(photo.pic.path)
            img = img.resize((800, 600))  # Resize to 800x600 or any desired size
            img.save(photo.pic.path)
        return redirect("home")
    context = {"categories": categories, "Photo": Photo}

    return render(request, "add_photo.html", context)


def delete_photo(request, pk):
    photo = Photo.objects.get(id=pk)
    if request.method == "POST":
        photo.delete()
        return redirect("home")
    context = {"photos": photo}
    return render(request, "delete_photo.html", context)


def edit_photo(request, pk):
    categories = Category.objects.all()  # Fetch all categories
    photo = Photo.objects.get(id=pk)  # Get the photo by its primary key
    if request.method == "POST":
        data = request.POST
        images = request.FILES.get("images")  # Get the uploaded image (if any)
        # Handle category selection
        if data["category"] != "none":
            category = Category.objects.get(id=data["category"])
        elif data["category_new"] != "":
            category, created = Category.objects.get_or_create(
                name=data["category_new"]
            )
        else:
            category = None
        photo.title = data["title"]  # Update the title of the photo
        # Update the category of the photo
        photo.category = category
        photo.description = data["description"]
        if images:
            photo.pic = images
        photo.save()
        return redirect("home")

    context = {
        "categories": categories,
        "photo": photo,
    }
    return render(request, "edit_photo.html", context)


def search(request):
    query = request.GET.get("q")  # Get the search query from the URL
    posts = (
        Photo.objects.filter(title__icontains=query) if query else []
    )  # Filter results
    return render(request, "search.html", {"query": query, "posts": posts})


def about(request):
    return render(request, "about.html")


# def home(request):
#     category = request.GET.get("category")  # Get the category from the request
#     if category is None:
#         photos = Photo.objects.all()
#     else:
#         photos = Photo.objects.filter(category__name=category)

#     categories = Category.objects.all()

#     # Pagination
#     paginator = Paginator(photos, 6)  # Show 6 photos per page
#     page_number = request.GET.get("page", 1)
#     page_obj = paginator.get_page(page_number)

#     if request.headers.get('x-requested-with') == 'XMLHttpRequest':  # Check if it's an AJAX request
#         photos_data = [
#             {
#                 "id": photo.id,
#                 "pic_url": photo.pic.url,
#                 "description": photo.description,
#             }
#             for photo in page_obj
#         ]
#         return JsonResponse({"photos": photos_data, "has_next": page_obj.has_next()})

#     context = {
#         "categories": categories,
#         "photos": page_obj,
#         "category": category,
#     }
#     return render(request, "index.html", context)
