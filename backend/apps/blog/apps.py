from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.blog'

    def ready(self):
        # 【知识点】导入创建的信号监听函数（而且 import 可以自带锁，不会出现异步问题）
        import apps.blog.signals
