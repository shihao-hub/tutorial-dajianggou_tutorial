from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path("test_index/", views.test_index, name="index"),
]
