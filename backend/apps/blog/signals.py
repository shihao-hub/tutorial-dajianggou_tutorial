"""
# Django 信号机制

> 参考链接：
>
> https://pythondjango.cn/django/advanced/10-signals/

---

把所以自定义的信号监听函数集中放在 app 对应文件夹下的 signals.py 文件里，便于后期集中维护。

---



"""

from django.dispatch import Signal

# 【知识点】自定义信号
#  非常清晰，@receiver(signal) <=> on 注册回调，signal.send <=> emit 触发信号执行回调（注意事件是同步的）
# str_msg_sender = Signal()


