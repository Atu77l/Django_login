from rest_framework import serializers
from .models import Register,Hello

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=Register
        fields=['name','email','password']
        
class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Hello
        fields="__all__"