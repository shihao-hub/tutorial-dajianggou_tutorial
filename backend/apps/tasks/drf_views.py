from rest_framework import decorators, views, mixins, generics, viewsets

from . import models, serializers


class TaskViewSet(viewsets.ModelViewSet):
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer
