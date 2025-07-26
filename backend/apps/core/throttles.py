from rest_framework import throttling

# See https://pythondjango.cn/django/rest-framework/10-throttling/


import random


class RandomRateThrottle(throttling.BaseThrottle):
    """该限流类 10 个请求中可能只有一个通过"""
    def allow_request(self, request, view):
        return random.randint(1, 10) != 1
