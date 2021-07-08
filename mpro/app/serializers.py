from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import AdminProfile, Attendencemodel, StudentsMainProfile, TeacherProfile, Dep,TecherMainProfile, StudentProfile, StudentEvulate,TeacherEvulate
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

class TeacherProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TecherMainProfile
        fields = '__all__'
        depth= 1

class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model= StudentProfile
        fields= '__all__'
        depth= 1

class Attendence(serializers.ModelSerializer):
    class Meta:
        model= Attendencemodel
        fields= '__all__'
        
class SEserializer(serializers.ModelSerializer):
    class Meta:
        model = StudentEvulate
        fields = '__all__'

class TEserilizers(serializers.ModelSerializer):
    class Meta:
        model= TeacherEvulate
        fields = '__all__'


class StudentprofileSerialuzer(serializers.ModelSerializer):
    class Meta:
        model= StudentsMainProfile
        fields = '__all__'
        depth = 1

        