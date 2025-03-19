from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='main'),
    path('add_photo/', views.add_photo, name='add_photo'),
    path('detailed_view/<str:pk>/', views.detailed_view, name='detailed_view'),
    path('about/', views.about, name='about'),
]
