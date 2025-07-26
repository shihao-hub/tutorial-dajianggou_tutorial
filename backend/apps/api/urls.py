from django.contrib import admin
from django.urls import path

from .api import api
from .mediator import register_views

register_views()

# todo: 确定一下必定如此吗？以及这个 register_views 函数难道必须每个项目都这样吗？没什么好办法自动吗？
# todo: 注意，app 下的 urls.py 似乎可以理解为 django app 入口，因为 include("apps.app.urls") 会被调用！
urlpatterns = [
    path("", api.urls),
]
