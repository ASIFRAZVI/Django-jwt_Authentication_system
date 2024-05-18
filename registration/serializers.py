from rest_framework import serializers
from .models import *


class user_registration_serializers(serializers.ModelSerializer):
    class Meta:
        model=Register_user
        fields='__all__'


class login_serializers(serializers.Serializer):
    username=serializers.CharField(max_length=100)
    password=serializers.CharField(max_length=100)