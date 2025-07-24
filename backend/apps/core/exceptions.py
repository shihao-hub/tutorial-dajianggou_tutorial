import uuid
import time
import traceback
from typing import Annotated, Any, Type

from loguru import logger

from django.conf import settings
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.views import exception_handler


class TypeCheckError(Exception):
    """类型检查出错"""

    def __init__(self, value: Any, expected_type: Type["object"]):
        super().__init__(f"期待 {expected_type} 类型，但是实际 {type(value)} 类型。")


class NotAllowedMethodError(Exception):
    """不允许调用的请求方法"""

    def __init__(self, method_name: str):
        super().__init__(f"不允许调用 {method_name} 方法。")


def _get_username(request):
    if not hasattr(request, "user"):
        return "Anonymous01"
    if not hasattr(request.user, "is_authenticated"):
        return "Anonymous02"
    return request.user.username


def _log_error_details(error_id, timestamp, timestamp_isoformat, request, exception, full_stack):
    """记录错误详情到日志系统"""

    log_message = [
        f"ERROR_ID: {error_id}",
        f"TIMESTAMP: {timestamp}",
        f"TIMESTAMP_ISOFORMAT: {timestamp_isoformat}",
        f"PATH: {request.path}",
        f"METHOD: {request.method}",
        f"USER: {_get_username(request)}"
    ]

    # 获取客户端 IP (安全方式)
    ip = request.META.get('HTTP_X_FORWARDED_FOR')
    if not ip:
        ip = request.META.get('REMOTE_ADDR', 'Unknown')
    else:
        ip = ip.split(',')[0]  # 取第一个 IP

    log_message.append(f"CLIENT_IP: {ip}")

    if exception:
        log_message.append(f"EXCEPTION: {type(exception).__name__}")
        log_message.append(f"MESSAGE: {str(exception)}")

    if full_stack and full_stack != "NoneType: None\n":
        log_message.append("FULL STACK TRACE:")
        log_message.append(full_stack)

    # 记录到日志系统
    logger.error("\n{}", '\n'.join(log_message))


def _detailed_500_response(request, exception=None):
    """
    生成包含调试信息的 500 错误响应
    :param request: Django request 对象
    :param exception: 捕获的异常对象 (可选)
    :return: DRF Response 对象
    """
    # 生成错误 ID (8 位十六进制)
    error_id = uuid.uuid4().hex  # uuid.uuid4().hex[:8] 实际项目中可增加长度到 12 位降低碰撞概率
    timestamp = time.time()
    timestamp_isoformat = timezone.now().isoformat()
    # 基础响应数据
    response_data = {
        "message": "Internal Server Error",
        "detail": "An unexpected error occurred. Please contact support with the error ID.",
        "timestamp": timestamp,
        "timestamp_isoformat": timestamp_isoformat,
        "error_id": error_id,
    }
    # 调试模式添加额外信息
    debug_info_enabled = False
    if settings.DEBUG and debug_info_enabled:
        debug_info = {
            "error_type": type(exception).__name__ if exception else "Unknown",
            "path": request.path,
            "method": request.method,
        }

        # 添加安全的异常消息
        if exception:
            # 过滤掉可能敏感的信息
            debug_info["message"] = str(exception).split('\n')[0][:200]  # 取首行并截断

        # 添加安全格式化的堆栈跟踪 (最后3行)
        stack_trace = traceback.format_exc()
        if stack_trace and stack_trace != "NoneType: None\n":
            debug_info["stack_trace"] = stack_trace.splitlines()[-3:]

        response_data["debug_info"] = debug_info
    # 记录完整错误到日志系统 (关键步骤!)
    _log_error_details(
        error_id=error_id,
        timestamp=timestamp,
        timestamp_isoformat=timestamp_isoformat,
        request=request,
        exception=exception,
        full_stack=traceback.format_exc()
    )
    return Response(response_data, status=500)


def global_exception_handler(exc, context):
    # 2025-07-23：以下内容由 ai 生成

    # 1. 先调用 DRF 默认异常处理
    response = exception_handler(exc, context)

    # 2. 处理未捕获的异常 (500 错误)
    if response is None:
        request = context['request']
        return _detailed_500_response(request, exc)

    # 3. 可选: 自定义其他错误格式
    return response
