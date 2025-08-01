"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name="home")
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name="home")
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path("blog/", include("blog.urls"))
"""
from django.urls import path, include, re_path
from django.conf import settings
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.core import register_signals

register_signals()  # 像这种预定义导入暂且放在此处，按照我的理解 urls.py 放这些不太合适

urlpatterns = [
    # drf 用户登录页面
    path("api-auth/", include("rest_framework.urls")),
    # drf 获取 Token
    path("api-token-auth/", obtain_auth_token),
    # rest_framework_simplejwt 获取和刷新 Token
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    # todo: 将此处的每个 app 视为一个小项目，让 ai 作为产品经理，给你提需求，你去完成
    path("v1/blog/", include("apps.blog.urls")),  # 【博客系统】DRF
    path("v1/tasks/", include("apps.tasks.urls")),  # 【任务列表】传统 Django，推荐用来练习 tailwind css
    path("v1/invitationcode/", include("apps.invitationcode.urls")),  # 【免登录邀请码】DRF
    path("v1/auth2/", include("apps.auth2.urls")),  # 【登录系统】DRF
    path("v1/bookmanagement/", include("apps.bookmanagement.urls")),  # 【图书管理系统】DRF
    path("v1/users/", include("apps.users.urls")),  # 【美观的管理后台】传统 Django，推荐用来练习 tailwind css

    path("v1/ninja/api/", include("apps.api.urls")),
]

# 【知识点】仅在开发环境启用 django admin 后台管理 和 drf_spectacular 交互式文档
if settings.DEBUG:
    from django.contrib import admin
    from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

    urlpatterns += [
        # django admin
        path("admin/", admin.site.urls),
        # drf_spectacular 交互式文档 -> [tip] 不同于 django，这个路由的后缀 / 必须指定，否则无法访问
        path("api/schema/", SpectacularAPIView.as_view(), name="api-schema"),
        path("api/docs/", SpectacularSwaggerView.as_view(url_name="api-schema"), name="swagger-ui"),
    ]

# 仅在开发环境提供静态文件服务
if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 【知识点】django-debug-toolbar
# See https://juejin.cn/post/6844903720304508935
if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [re_path("^__debug__/", include(debug_toolbar.urls)), ] + urlpatterns
