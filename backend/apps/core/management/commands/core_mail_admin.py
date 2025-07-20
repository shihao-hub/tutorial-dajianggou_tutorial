from datetime import timedelta, time, datetime

from django.core.mail import mail_admins
from django.core.management import BaseCommand
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()

today = timezone.now()
yesterday = today - timedelta(1)


# reference link: https://pythondjango.cn/django/advanced/11-django-admin-commands/

class Command(BaseCommand):
    help = "Send The Daily Count of New Users to Admins"

    def handle(self, *args, **options):
        # 获取过去一天注册用户数量
        user_count = User.objects.filter(date_joined__range=(yesterday, today)).count()

        # 当注册用户数量多余1个，才发送邮件给管理员
        if user_count >= 1:
            message = "You have got {} user(s) in the past 24 hours".format(user_count)

            subject = (
                f"New user count for {today.strftime('%Y-%m-%d')}: {user_count}"
            )

            mail_admins(subject=subject, message=message, html_message=None)

            self.stdout.write("E-mail was sent.")
        else:
            self.stdout.write("No new users today.")
