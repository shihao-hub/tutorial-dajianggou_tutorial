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
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    # django admin
    path('admin/', admin.site.urls),
    # drf_spectacular
    path('api/schema/', SpectacularAPIView.as_view(), name='api-schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='api-schema'), name='swagger-ui'),

    path("blog/", include("apps.blog.urls")),
    path("tasks/", include("apps.tasks.urls")),
]

# 【知识点】django-debug-toolbar
# See https://juejin.cn/post/6844903720304508935
if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [re_path('^__debug__/', include(debug_toolbar.urls)), ] + urlpatterns
