import os
import logging

from waitress import serve

from django.core.wsgi import get_wsgi_application

logger = logging.getLogger("waitress")
logger.setLevel(logging.DEBUG)

# 设置环境变量
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

# 获取 WSGI 应用
application = get_wsgi_application()

# todo: drf_spectacular 会访问 cdn 的资源，这资源我需要翻墙...

if __name__ == "__main__":
    # 启动服务
    serve(
        application,
        host="0.0.0.0",
        port=8000,
        threads=4,  # 推荐线程数 = (核心数 * 2) + 1
        # url_scheme="https"  # 如果使用 HTTPS 需要设置
    )
