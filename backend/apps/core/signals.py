from loguru import logger

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    # 在创建用户时自动生成 token
    if created:
        Token.objects.create(user=instance)
        logger.info("在创建用户时自动生成 token 成功")
