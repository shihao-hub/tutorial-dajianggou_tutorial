from django.contrib import admin

from . import models


@admin.register(models.Book)  # 使用 register 的装饰器
class BookAdmin(admin.ModelAdmin):
    pass

# admin.site.register(models.Book, BookAdmin) #  使用 register 的方法
