from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/special:search", views.search, name = "search"),
    path("wiki/<str:title>", views.display, name = "display"),
    path("wiki/new",views.create_new_entry, name = "create_new_entry")
]


