from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy


class TaskStatus(models.TextChoices):
    UNSTARTED = "u", gettext_lazy("尚未开始")
    ONGOING = "o", gettext_lazy("正在进行中")
    FINISHED = "f", gettext_lazy("已完成")


class Task(models.Model):
    user = models.ForeignKey(User, verbose_name="所属人", on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(verbose_name="任务名", max_length=100)
    status = models.CharField(verbose_name="任务状态", max_length=1, choices=TaskStatus.choices,
                              default=TaskStatus.UNSTARTED)
    content = models.CharField(verbose_name="任务内容", max_length=1000)
    due_date = models.DateTimeField(verbose_name="截止日期", null=True, blank=True)
    created_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    updated_time = models.DateTimeField(verbose_name="更新时间", auto_now=True)
    is_deleted = models.BooleanField(verbose_name="是否删除", default=False)

    class Meta:
        verbose_name = verbose_name_plural = "任务"

    def __str__(self):
        if self.user is None:
            return self.name
        return f"{self.user.username}:{self.name}"
