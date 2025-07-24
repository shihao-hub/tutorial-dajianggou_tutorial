from django.urls import path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r"", viewset=views.AuthViewSet, basename="auth")

app_name = "auth"

urlpatterns = [
    # path("", views.LoginView.as_view(), name="login"),
    # path("logout/", views.LogoutView.as_view(), name="logout"),
    # path("register/", views.RegisterView.as_view(), name="register"),
]

urlpatterns += router.urls
