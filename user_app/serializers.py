from rest_framework import serializers


class RegistrationSerializer(serializers.Serializer):
    firstName = serializers.CharField(max_length=50)
    lastName = serializers.CharField(max_length=50)
    email = serializers.EmailField(max_length=50)
    userName = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=50)
    mobileNo = serializers.IntegerField()
    age = serializers.IntegerField()


class LoginSerializer(serializers.Serializer):
    userName = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)
