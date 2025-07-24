from django.urls import path

from . import views

# 感想：
# 1. 这个小应用的实践过程中，才发现前面学习的内容又忘记了不少，果然，理论 + 实践必须齐头并进！
# 2. 大江狗教程的 drf 内容还是太少了，不够全面

app_name = "invitationcode"
urlpatterns = [
    # todo: 确定一下 drf 中 path 的 name 参数还有什么用吗？
    path("", views.InvitationCodeAPIView.as_view()),
]
