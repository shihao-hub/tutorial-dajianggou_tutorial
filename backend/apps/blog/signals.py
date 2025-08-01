from django.dispatch import Signal

# 【知识点】自定义信号
#   非常清晰，@receiver(signal) <=> on 注册回调，signal.send <=> emit 触发信号执行回调（注意事件是同步的）
#   https://pythondjango.cn/django/advanced/10-signals/
# str_msg_sender = Signal()


