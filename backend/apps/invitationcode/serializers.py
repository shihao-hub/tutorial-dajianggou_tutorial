from rest_framework import serializers

from . import models


class InvitationCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.InvitationCode
        fields = '__all__'
