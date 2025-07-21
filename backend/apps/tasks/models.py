from django.db import models
from django.utils.translation import gettext_lazy


class TaskStatus(models.TextChoices):
    UNSTARTED = "u", gettext_lazy("尚未开始")
    ONGOING = "o", gettext_lazy("正在进行中")
    FINISHED = "f", gettext_lazy("已完成")




class Task(models.Model):
    name = models.CharField(verbose_name="任务名", max_length=100)
    status = models.CharField(verbose_name="任务状态", max_length=1, choices=TaskStatus.choices)
    content = models.CharField(verbose_name="任务内容", max_length=1000)

    # 待定，需要确定 django 自动 form 的规格
    # created_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    # updated_time = models.DateTimeField(verbose_name="更新时间", auto_now=True)
    # is_deleted = models.BooleanField(verbose_name="是否删除", default=False)

    def __str__(self):
        return self.name
