from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class TokenObtainPairSerializerCustomized(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(TokenObtainPairSerializerCustomized, cls).get_token(user)

        # 在 payload 部分提供更多信息
        token['username'] = user.username
        return token
