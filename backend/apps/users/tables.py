import django_tables2 as tables
from django.utils.html import format_html
from django.urls import reverse

from . import models


class UserTable(tables.Table):
    id_select = tables.CheckBoxColumn(accessor="id", orderable=False, exclude_from_export=True)
    actions = tables.Column(empty_values=(), verbose_name="操作", orderable=False, exclude_from_export=True)

    class Meta:
        model = models.User
        fields = ["username", "email", "first_name", "last_name", "is_staff"]
        sequence = ["id_select"] + fields + ["actions"]  # 表格中字段显示顺序
        template_name = "users/bs4_tables2.html"  # 表格模板
        attrs = {"class": "table table-striped table-sm text-nowrap"}  # 表格样式
        order_by_field = "sort_by"  # 排序字段（default: sort）
        # page_field = "page"

    def render_actions(self, value, record):
        """自定义操作链接"""
        # 【知识点】Boostrap 4
        return format_html(
            '<a class="btn btn-sm badge badge-pill badge-warning ml-2" href= "' +
            reverse("users:user_update", args=[str(record.pk)]) + '">' + '编辑' + '</a>'
            + '<a class=" btn  btn-sm badge badge-pill badge-danger ml-2" href= "' +
            reverse("users:user_delete", args=[str(record.pk)]) + '">' + '删除' + '</a>'
        )
