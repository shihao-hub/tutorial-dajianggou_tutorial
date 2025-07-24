from rest_framework import serializers

from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ("username", "password")

    # todo: 进行密码验证服务（简单点，通过校验 password 计算值与数据库的值）
