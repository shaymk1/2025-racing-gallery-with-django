from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("add_photo/", views.add_photo, name="add_photo"),
    path("delete_photo/<str:pk>/", views.delete_photo, name="delete_photo"),
    path("photo/<int:pk>/edit/", views.edit_photo, name="edit_photo"),
    path("detailed_view/<str:pk>/", views.detailed_view, name="detailed_view"),
    path("search/", views.search, name="search"),
    path("about/", views.about, name="about"),
]
