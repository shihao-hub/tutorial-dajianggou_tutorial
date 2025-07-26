"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from rest_framework.authtoken.views import obtain_auth_token
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.core import register_signals

register_signals()  # 像这种预定义导入暂且放在此处，按照我的理解 urls.py 放这些不太合适

urlpatterns = [
    # django admin
    path('admin/', admin.site.urls),
    # drf_spectacular 交互式文档
    path('api/schema/', SpectacularAPIView.as_view(), name='api-schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='api-schema'), name='swagger-ui'),
    # drf 用户登录页面
    path('api-auth/', include('rest_framework.urls')),
    # drf 获取 Token
    path('api-token-auth/', obtain_auth_token),
    # rest_framework_simplejwt 获取和刷新 Token
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path("v1/blog/", include("apps.blog.urls")),
    path("v1/tasks/", include("apps.tasks.urls")),
    path("v1/invitationcode/", include("apps.invitationcode.urls")),
    path("v1/auth2/", include("apps.auth2.urls")),

    path("v1/ninja/api/", include("apps.api.urls")),
]

# 【知识点】django-debug-toolbar
# See https://juejin.cn/post/6844903720304508935
if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [re_path('^__debug__/', include(debug_toolbar.urls)), ] + urlpatterns
