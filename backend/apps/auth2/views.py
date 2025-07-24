from rest_framework import views, decorators, generics, viewsets
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from . import serializers


class AuthViewSet(viewsets.ViewSet):
    @extend_schema(request=serializers.UserSerializer)
    @action(methods=["POST"], detail=False)
    def register(self, request: Request) -> Response:
        """
        用户注册：创建新账户
        """
        return Response({"message": "Register successful"})

    @extend_schema(request=serializers.UserSerializer)
    @action(methods=["POST"], detail=False)
    def login(self, request: Request) -> Response:
        """
        用户登录：验证用户凭据
        """
        return Response({"message": "Login successful"})

    @action(methods=["POST"], detail=False)
    def logout(self, request: Request) -> Response:
        """
        用户注销：安全结束会话
        """
        return Response({"message": "Logout successful"})
