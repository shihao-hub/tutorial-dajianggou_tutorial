from typing import override

from rest_framework import pagination
from rest_framework.response import Response


# todo: 学习一下 rest_framework 的项目结构，根本不需要多层嵌套，单个文件足以，一个文件 1000 行内，争取不要拆分！假如感觉乱糟糟的，那必然是自己抽象的问题！ # noqa
class PageNumberPaginationCustomized(pagination.PageNumberPagination):
    page_size = 2  # 每页默认展示数据的条数
    page_size_query_param = "size"  # 每页 size 的参数名
    max_page_size = 10  # 每个可以展示的最大数据条数

    @override
    def get_paginated_response(self, data):
        return Response({
            "links": {
                "next": self.get_next_link(),
                "previous": self.get_previous_link()
            },
            "count": self.page.paginator.count,
            "results": data
        })


class LimitOffsetPaginationCustomized(pagination.LimitOffsetPagination):
    default_limit = 5  # default limit per age
    limit_query_param = "limit"  # default is limit
    offset_query_param = "offset"  # default param is offset
    max_limit = 10  # max limit per age


# cursor=xxx 会进行加密
# 并不推荐全局使用自定义的 CursorPagination 类，更好的方式是在 GenericsAPIView 或视图集 viewsets 中通过 pagination_class 属性指定
class CursorPaginationCustomized(pagination.CursorPagination):
    page_size = 3  # Default number of records per age
    page_size_query_param = "page_size"
    cursor_query_param = "cursor"  # Default is cursor
    ordering = "-create_date"
