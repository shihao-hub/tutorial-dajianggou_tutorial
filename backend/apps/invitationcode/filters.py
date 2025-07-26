import django_filters

from . import models


# todo: 被使用的时候需要将权限设置为仅限管理员，因为邀请码肯定不允许非管理员看见
class InvitationCodeFilter(django_filters.FilterSet):
    q = django_filters.CharFilter(field_name="code", lookup_expr="contains")

    class Meta:
        model = models.InvitationCode
        fields = ('code',)
