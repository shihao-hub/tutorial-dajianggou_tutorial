from rest_framework import serializers


class InvitationCodeValidationSchema(serializers.Serializer):
    """邀请码验证请求体"""
    code = serializers.CharField(
        max_length=6,
        min_length=1,
        required=True,
        help_text="邀请码"
    )
