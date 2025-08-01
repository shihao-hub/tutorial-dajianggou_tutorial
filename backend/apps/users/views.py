from typing import override

from django_tables2 import SingleTableView, RequestConfig
from django_filters.views import FilterView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from . import filters, forms, models, tables


# ==================================== Django View ==================================== #
class UserAdminTableView(LoginRequiredMixin, SingleTableView, FilterView):
    filter = None
    filter_class = filters.UserFilter  # 使用 UserFilter 过滤
    table_class = tables.UserTable  # 使用 UserTable 展示数据
    template_name = "users/user_admin_list.html"

    @override
    def get_queryset(self, **kwargs):
        """获取过滤后的查询集"""
        qs = models.User.objects.all().order_by("-id")
        self.filter = self.filter_class(self.request.GET, queryset=qs)
        return self.filter.qs

    @override
    def get_context_data(self, **kwargs):
        """将查询集与 table 实例集合，提供 filter 和 table 两个变量前端渲染"""
        context = super().get_context_data(**kwargs)
        t = self.table_class(data=self.get_queryset())
        # 每页 5 条记录
        RequestConfig(self.request, paginate={"per_page": 5}).configure(t)
        context["filter"] = self.filter
        context["table"] = t
        return context


class UserListView(generic.ListView):
    model = models.User
    template_name = "users/user_list.html"  # {app_name}_list.html -> 列表展示数据


class UserCreateView(generic.CreateView):
    model = models.User
    template_name = "users/user_form.html"  # [C] {app_name}_form.html -> 创建的表单
    form_class = forms.UserForm
    success_url = reverse_lazy("users:user_admin_list")  # 创建成功，重定向至 list.html


class UserDeleteView(generic.DeleteView):
    form_class = forms.UserForm
    template_name = "users/user_confirm_delete.html"  # [D] {app_name}_confirm_delete.html -> 确认删除页面
    success_url = reverse_lazy("users:user_admin_list")  # 删除成功，重定向至 list.html


class UserUpdateView(generic.UpdateView):
    model = models.User
    template_name = "users/user_form.html"  # [U] {app_name}_form.html -> 创建的表单，但有数据渲染
    form_class = forms.UserForm
    success_url = reverse_lazy("users:user_admin_list")  # 更新成功，重定向至 list.html


class UserDetailView(generic.DetailView):
    model = models.User

# todo: [链接](https://pythondjango.cn/django/applications/1-django-filter-table2/)
#       未完成，因为教程不完整，需要关注，但是公众号没找到...
#       不完整的部分主要是 templates/users/*.html 模板文件...
