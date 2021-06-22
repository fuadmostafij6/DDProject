from django.db.models import fields
from rest_framework import serializers
from .models import AdminProfile, TeacherProfile, Dep
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token




User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", 'username', 'password', 'first_name', 'last_name', 'email')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        AdminProfile.objects.create(prouser=user)
        return user


class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = AdminProfile
        fields = "__all__"
        read_only_fields = ['adminuser']

    def validate(self, attrs):
        attrs['adminuser'] = self.context['request'].user
        return attrs

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['adminuser'] = UserSerializer(instance.adminuser).data
        return response



class TeacherAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherProfile
        fields = '__all__'
        

class DepSerializer(serializers.ModelSerializer):
    class Meta:
        model= Dep
        fields ='__all__'
    

    
