from django.contrib import admin

from . import models


# 通过 django 自带的 admin 对邀请码进行管理
class InvitationCodeAdmin(admin.ModelAdmin):
    list_display = ("code", "expire")

    class Meta:
        model = models.InvitationCode


admin.site.register(models.InvitationCode, InvitationCodeAdmin)
