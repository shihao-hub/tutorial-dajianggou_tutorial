import django_filters
from django.db.models import Q

from . import models


class UserFilter(django_filters.FilterSet):
    query = django_filters.CharFilter(method="customized_filter", label="关键词")

    class Meta:
        model = models.User
        fields = {
            "is_staff",
            "is_superuser",
            "is_active"
        }

    def customized_filter(self, queryset, q, value):
        return queryset.filter(Q(username__icontains=value) | Q(email__icontains=value))
