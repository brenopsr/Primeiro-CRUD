from django.contrib import admin
from django.urls import path, include
from triup.website import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("tasks.urls")),
    path("", views.home, name="home"),
]
