import json
import uuid

from loguru import logger

from django.conf import settings
from django.http.response import HttpResponse
from django.utils import timezone
from rest_framework.response import Response


class GlobalExceptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_exception(self, request, exception):
        logger.error(f"Unhandled Exception: {str(exception)}", exc_info=True)

        data = {
            "message": "Internal Server Error",
            "detail": "An unexpected error occurred. Please contact the administrator.",
            "timestamp": timezone.now().isoformat(),  # ISO 8601 格式时间
            "error_id": uuid.uuid4().hex[:8],  # 唯一错误 ID 用于日志追踪（日志中也需要统一记录）
        }
        if settings.DEBUG:
            pass
        # return Response(data, status=500)
        return HttpResponse(json.dumps(data).encode("utf-8"), status=500)
