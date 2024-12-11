from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.exceptions import ValidationError
from django.contrib.auth.models import User


MIN_LENGTH  = 8

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=MIN_LENGTH, error_messages = { "min_length": f"Password must be longer than {MIN_LENGTH} charaters"})
    password2 =serializers.CharField(write_only=True, min_length=MIN_LENGTH, error_messages= { "min_length": f"Password must be longer than {MIN_LENGTH} characters"})

    class Meta:
        model = User
        fields = "__all__"

    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError("Password does not match")

        return data

    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data["username"],
            email= validated_data["email"],
            first_name = validated_data["first_name"],
            last_name= validated_data["last_name"],
            
        )

        user.set_password(validated_data["password"])
        user.save()

        return user


class LoginSerializer(serializers.Serializer):

    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True)

    
    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")
       
        user = authenticate(username=username , password=password)

        if user is None:
            raise ValidationError("Identifiants incorrects.")

 
        attrs['user'] = user
        

        return attrs