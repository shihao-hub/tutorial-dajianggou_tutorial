from typing import Union

from django.http import HttpRequest
from rest_framework import views, decorators, generics, viewsets, status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from . import models, serializers


class AuthViewSet(viewsets.ViewSet):
    """
    使用手册：
        url: /register
        method: POST
        body: {"username": "string", "password": "string"}
        use effect: 创建新用户

        url: /login
        method: POST
        body: {"username": "string", "password": "string"}
        use effect: 用户登录，记录 session，用来进行权限认证（request.session 由后台设置，安全性足够）

        url: /logout
        method: POST
        body: {"username": "string", "password": "string"}
        use effect: 用户注销，删除 session

    """
    @extend_schema(request=serializers.MyUserSerializer)
    @action(methods=["POST"], detail=False)
    def register(self, request: Union[HttpRequest, Request]) -> Response:
        """
        用户注册：创建新账户
        """
        serializer = serializers.MyUserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response({"message": "用户注册成功"})

    @extend_schema(request=serializers.MyUserSerializer)
    @action(methods=["POST"], detail=False)
    def login(self, request: Union[HttpRequest, Request]) -> Response:
        """
        用户登录：验证用户凭据
        """
        # todo: 提前校验？类似 fastapi 吗？还是怎么说？serializers.MyUserSerializer 是否可以校验？还是说 save 才会出问题，单纯校验不会？
        user = models.MyUser.objects.filter(username=request.data["username"]).first()
        if not user:
            return Response({"message": "用户登录失败，用户名不存在"}, status=status.HTTP_400_BAD_REQUEST)
        if user.password != request.data["password"]:
            return Response({"message": "用户登录失败，密码不正确"}, status=status.HTTP_400_BAD_REQUEST)
        # 验证成功，设置 session
        # todo: 是否应该是创建一个和 username 和 password 关联的唯一数据？并设置其有效期？而不是用 session
        request.session[user.username] = True
        return Response({"message": "用户登录成功"})

    @extend_schema(request=serializers.MyUserSerializer)
    @action(methods=["POST"], detail=False)
    def logout(self, request: Union[HttpRequest, Request]) -> Response:
        """
        用户注销：安全结束会话
        """
        # todo: 确定一下，如何注销？是否需要发送账号密码？
        user = models.MyUser.objects.filter(username=request.data["username"]).first()
        if not user:
            return Response({"message": "用户注销失败，用户名不存在"}, status=status.HTTP_400_BAD_REQUEST)
        if user.password != request.data["password"]:
            return Response({"message": "用户注销失败，密码不正确"}, status=status.HTTP_400_BAD_REQUEST)
        # 清除 session
        del request.session[user.username]
        return Response({"message": "用户注销成功"})
