from rest_framework import serializers
from ..models import Request, Log

class  RequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Request
        fields = '__all__'
        extra_kwargs = {
            'user_id': {'read_only': True, 'required': False},
            'time': {'required': False},
            'key': {'required': False},
        }

class ConfirmSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    key = serializers.CharField(max_length=255)

    class Meta:
        fields = ('user_id','key',)
        extra_kwargs = {
            'user_id': {'required': True},
            'key': {'required': True},
        }
class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log    
        fields = '__all__'
        extra_kwargs = {
            'user_id': {'read_only': True, 'required': False},
            'group_id': {'read_only': True, 'required': False},
            'key': {'required': False},
        }
