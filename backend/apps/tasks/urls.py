from django.urls import path

from . import views

app_name = "tasks"

# todo: 需要确定一下，每次响应的都是 html（是否耗时？），这种传统的 web 开发是否已经过时了？

# reference link: https://pythondjango.cn/django/applications/2-django-CBV-CRUD-example/
#
# Django 实战：使用通用类视图开发任务管理 CRUD 小应用
#   - 创建指定目录下指定命名的 .html 文件
#   - ListView、CreateView、DeleteView、UpdateView、DetailView 五个视图类绑定指定 model
#   - 注册 urls
# 只需要以上三步，不需要编写额外代码，基础的 CRUD 应用即可实现。
# 如果需要扩展，通过 hook 也能实现大部分功能。
#
# 【知识点】下文需要反复阅读，反复实践！
# 至此，让我联想到：https://pythondjango.cn/django/rest-framework/3-CBV-APIView-viewsets/
# 此文是关于 drf 的 APIView、Mixin and GenericAPI、generics.*、ViewSet 四种类的视图
# 四种类的视图概览：
#   - APIView 基本上等价于 django View 的高级封装，基础的 get post 等未修改，但是新增了不少高级功能，如限流？（直接看 APIView 源码）
#   - 基础的 APIView 类并没有大量简化我们的代码，仔细观察，会发现与增删改查操作相关的代码包括返回内容对所有模型几乎都是一样的。
#     对于这些通用的增删改查行为，DRF 已经提供了相应的 Mixin 类。Mixin 类可与 generics.GenericAPI 类联用，灵活组合成你所需要的视图。
#   - DRF 还提供了一套常用的将 Mixin 类与 GenericAPI 类已经组合好了的视图 -> generics.*
#   - 使用视图集可以进一步减少代码重复
# 呃，一步一步封装，越来越简化，越来越面向配置了。
# 为什么要使用基于类的视图：
#   - 函数视图的代码的复用率非常低。
#   - 类视图可以有效的提高代码复用，因为类是可以被继承的，可以拓展的。
#     特别是将一些可以共用的功能抽象成Mixin类或基类后可以减少重复造轮子的工作。
# 结论：
#   - 基础的 APIView 类：可读性最高、代码最多、灵活性最高。当你需要对的 API 行为进行个性化定制时，建议使用这种方式。
#   - 至于 mixin 类和 GenericAPI 的混用，这个和 generics 类没什么区别，不看也罢。
#   - 通用 generics 类：可读性好、代码适中、灵活性较高。当你需要对一个模型进行标准的增删查改全部或部分操作时建议使用这种方式。
#   - 使用视图集 Viewset: 可读性较低、代码最少、灵活性最低。当你需要对一个模型进行标准的增删查改的全部操作且不需定制 API 行为时建议使用这种方式。
#     但这是以牺牲了代码的可读性为代价的，因为它对代码进行了高度地抽象化。另外 urls由 router 生成，不如自己手动配置的清楚。


urlpatterns = [
    path("test/", views.TestView.as_view(), name="test"),

    path("", views.TaskListView.as_view(), name="task_list"),

    path("create/", views.TaskCreateView.as_view(), name="task_create"),
    path("delete/<int:pk>/", views.TaskDeleteView.as_view(), name="task_delete"),
    path("update/<int:pk>/", views.TaskUpdateView.as_view(), name="task_update"),
    path("detail/<int:pk>/", views.TaskDetailView.as_view(), name="task_detail"),
]


# djangorestframework
def _register_djangorestframework_urls():
    from rest_framework import routers, serializers
    from . import drf_views  # just a test

    global urlpatterns

    router = routers.DefaultRouter()
    # 【知识点】drf 的 router 末尾不允许添加 / ！
    #  此处符合 restful 风格，批量生成了：
    #   - /tasks/drf/ -> get - 列出列表、post - 创建实例
    #   - /tasks/drf/<int:pk>/ -> put - 全量更新、patch - 部分更新、get - 查询详情、delete - 删除实例
    router.register(r"drf", viewset=drf_views.TaskViewSet)

    urlpatterns += router.urls


_register_djangorestframework_urls()

# urlpatterns = format_suffix_patterns(urlpatterns)
