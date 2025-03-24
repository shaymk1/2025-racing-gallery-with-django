from django.contrib import admin
from django.urls import include, path
# import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("app.urls")),
]


# urlpatterns += staticfiles_urlpatterns()
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
