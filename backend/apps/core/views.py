from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from . import serializers


class AuthTokenCustomized(ObtainAuthToken):
    """
    DRF Token 定制化 <br>
    使用方法：<br>
        urls.py 文件中：path('api-token-auth/', AuthTokenCustomized.as_view()), <br>
    """

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        # todo: 确定一下如何设置失效时间
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })


class TokenObtainPairViewCustomized(TokenObtainPairView):
    """
    自定义令牌（Token）<br>
    使用方法：<br>
        path('token/', TokenObtainPairViewCustomized.as_view(), name='token_obtain_pair'),

    """
    permission_classes = (AllowAny,)
    serializer_class = serializers.TokenObtainPairSerializerCustomized
