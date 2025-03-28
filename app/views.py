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

    # search_query = request.GET.get("search")
    # if search_query:
    #     photos = photos.filter(description__icontains=search_query) # filter photos based on search query
    # for pagination
    # page_number = request.GET.get("page")
    # paginator = Paginator(photos, 10)  # Show 10 photos per page


def detailed_view(request, pk):
    photos = Photo.objects.get(id=pk)
    context = {"photos": photos}
    return render(request, "detailed.html", context)


def about(request):
    return render(request, "about.html")


def search(request):
    # for search query
    # Check if the request is a post request.
    if request.method == "GET":
        # Retrieve the search query entered by the user
        search_query = request.Get.get["search_query"]
        # Filter your model by the search query
        posts = Photo.objects.filter(title__icontains=search_query)
    return render(request, "search.html", {"query": posts, "posts": posts})
