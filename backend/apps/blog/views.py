from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse

from ..core import exceptions


def test_index(request: HttpRequest):
    if request.method not in ["GET"]:
        raise exceptions.NotAllowedMethodError(request.method)
    return HttpResponse(b"<body>blog:test_index</body>")
