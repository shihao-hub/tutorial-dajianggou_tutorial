import re
from typing import override

from loguru import logger

from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from . import models


class MyUserSerializer(serializers.ModelSerializer):
    """MyUser model 的 ModelSerializer 类，主要负责 MyUser model 的存储"""
    # 【知识点】覆盖自动生成的字段
    password = serializers.CharField(
        write_only=True,  # 确保密码不会在响应中返回
        style={"input_type": "password"},  # 为可浏览 API 提供提示
        min_length=8,  # 最小长度要求
        max_length=128,  # 最大长度限制
        trim_whitespace=False,  # 保留密码中的空格
        required=True  # 创建用户时必须提供密码
    )

    class Meta:
        model = models.MyUser
        fields = ("username", "password")
        # 【知识点】字段额外参数
        extra_kwargs = {
            "username": {"min_length": 3, "max_length": 30}
        }

    def validate_username(self, value):
        # 检查用户名是否已被使用
        if models.MyUser.objects.filter(username__iexact=value).exists():
            raise serializers.ValidationError("用户名已被使用")
        # todo: 校验用户名的格式，Schema 库如何？暂时使用要求只支持英文
        pattern = re.compile(r"^[a-zA-Z]*$")
        if not pattern.match(value):
            raise serializers.ValidationError("用户名只支持纯英文")
        return value

    def validate_password(self, value):
        # todo: 确定一下，此处的校验是最后才走吗？

        # todo: 验证密码强度（可以参考 django 的 validate_password 函数）
        vaild_password = True
        if not vaild_password:
            raise serializers.ValidationError("密码强度不够")

        return value

    def _get_password(self, validated_data):
        # todo: 拿到密码，并处理哈希
        return validated_data["password"]

    @override
    def create(self, validated_data):
        # todo: 确定一下何时会走入 create 函数

        logger.debug("[MyUserModelSerializer#create] start")
        user = models.MyUser(username=validated_data["username"])
        user.password = self._get_password(validated_data)
        user.save()
        return user

    @override
    def update(self, instance, validated_data):
        logger.debug("[MyUserModelSerializer#update] start")
        # 更新用户名（如果提供）
        instance.username = validated_data.get("username", instance.username)

        # 如果提供了新密码，则更新密码
        if "password" in validated_data:
            instance.password = self._get_password(validated_data)

        instance.save()
        return instance


# todo: 确定一下真的需要吗，和 UserSerializer 一些重复，要么不添加要么试一下能不能复用？
class LoginSerializer(serializers.Serializer):
    """用于登录验证的独立序列化器"""
    username = serializers.CharField()
    password = serializers.CharField(
        style={"input_type": "password"},
        trim_whitespace=False
    )

    def _authenticate(self, request, username, password) -> models.MyUser:
        return models.MyUser.objects.filter(username=username, password=password).first()

    @override
    def validate(self, attrs):
        """验证用户名和密码是否正确"""
        username = attrs.get("username")
        password = attrs.get("password")

        # 尝试认证用户
        user = self._authenticate(self.context.get("request"), username, password)

        if not user:
            # 认证失败
            raise serializers.ValidationError("用户名或密码不正确")

        # 检查用户是否激活
        if not user.is_active:
            raise serializers.ValidationError("用户账户已被禁用")

        # 将用户对象添加到验证数据中
        attrs["user"] = user
        return attrs
