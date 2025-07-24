from django.utils.timezone import now
from django.contrib import messages
from rest_framework import views, generics, viewsets
from rest_framework.request import Request
from rest_framework.response import Response

from . import models


def get_client_ip(request):
    """获取用户IP地址"""
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip


class InvitationCodeAPIView(views.APIView):
    def post(self, request: Request):
        """验证邀请码是否正确"""
        session_key = f"user_ip_{get_client_ip(request)}"
        # todo: 确定一下，post 不是创建吗？这样的话，验证的语义在哪里表达呢？好麻烦，restful api，怪异。。
        # todo: 确定一下，如果前台发送的是表单，request.data 和 application/json 结构一样吗？
        code = request.data["code"]
        # todo: Schema
        if not code:
            return Response({"message": "请求格式不正确"}, status=400)
        # 获得验证码
        code_inst = models.InvitationCode.objects.filter(code=code, expire__gte=now()).first()
        if not code_inst:
            # 删除会话记录，直接视其为过期
            if session_key in request.session:
                del request.session[session_key]
            return Response(data={"message": "验证码无效"}, status=500)
        # 验证码有效，设置此次会话的有效期为：60s
        # todo: 确定一下这个 session 难道只能存一个 key？好像不是，只是整个会话 60s 过期，但是假如这个 session 还有其他 key value 要使用呢？
        request.session[session_key] = code_inst.pk
        request.session.set_expiry(60)  # 整个 session？不能指定 key 吗？
        return Response(data={"message": "验证码有效，会话有效时间为 60s"})

    def get(self, request: Request):
        """访问验证码页面，根据 session 响应不同内容"""
        session_key = f"user_ip_{get_client_ip(request)}"
        if session_key in request.session:
            return Response(data={"message": "验证码有效，展示隐私内容"})
        return Response(data={"message": "验证码无效，无法查看隐私内容"})
