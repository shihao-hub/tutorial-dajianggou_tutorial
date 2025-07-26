from django.db import models


class MyUser(models.Model):
    # max_length 主要指定数据库字段的最大长度，并不属于校验，真正的校验交给 drf Serializer
    username = models.CharField(verbose_name="用户名", max_length=255, unique=True)
    password = models.CharField(verbose_name="密码", max_length=255)
    is_active = models.BooleanField(verbose_name="是否激活", default=True)
