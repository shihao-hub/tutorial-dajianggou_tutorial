from django.core.management.base import BaseCommand


# reference link: https://pythondjango.cn/django/advanced/11-django-admin-commands/

class Command(BaseCommand):
    help = "Print Hello World!"  # 帮助文本, 一般备注命令的用途及如何使用。

    def add_arguments(self, parser):
        """处理命令行参数，可选"""
        # 【知识点】此处使用的是 argparse 内置库，给命令添加一个名为 name 的参数
        parser.add_argument("name")

    def handle(self, *args, **options):
        """核心业务逻辑"""
        # 注意：当你使用管理命令并希望在控制台输出指定信息时，你应该使用 `self.stdout` 和 `self.stderr` 方法，
        # 而不能直接使用 python 的 `print` 方法。另外，你不需要在消息的末尾加上换行符，它将被自动添加。
        msg = "Hello World ! " + options["name"]
        self.stdout.write(msg)
