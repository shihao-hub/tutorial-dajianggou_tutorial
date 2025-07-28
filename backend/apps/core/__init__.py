def register_signals():
    from . import signals


# django 默认似乎导入 app 目录下的 admin.py 文件
def register_admin():
    from . import admin
