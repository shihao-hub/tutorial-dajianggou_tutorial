from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path("admin/list/", views.UserAdminTableView.as_view(), name="user_admin_list"),

    # 【知识点】【反复学习】传统 Django 实践
    path("list/", views.UserListView.as_view(), name="user_list"),  # get
    path("create/", views.UserCreateView.as_view(), name="user_create"),  # get/post
    path("delete/<int:pk>/", views.UserDeleteView.as_view(), name="user_delete"),  # post
    path("update/<int:pk>/", views.UserUpdateView.as_view(), name="user_update"),  # get/post
    path("detail/<int:pk>/", views.UserDetailView.as_view(), name="user_detail"),  # get
]
