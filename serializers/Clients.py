from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.exceptions import ValidationError
from django.contrib.auth.models import User
from Clients.models import Client

MIN_LENGTH  = 8

class UserSerializer(serializers.ModelSerializer):

    
    password = serializers.CharField(write_only=True, min_length=MIN_LENGTH, error_messages = { "min_length": f"Password must be longer than {MIN_LENGTH} charaters"})
    password2 =serializers.CharField(write_only=True, min_length=MIN_LENGTH, error_messages= { "min_length": f"Password must be longer than {MIN_LENGTH} characters"})

    class Meta:
        model = User
        fields = ['username', 'email','password', 'password2', ]

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
        client = Client.bbjects.create(user=user)

        return user

class ClientSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Client
        fields = ['user','adresse' ,'telephone', ]

    def validate(self, data):
        if data['user']['password'] != data['user']['password2']:
            raise serializers.ValidationError("password does not match")
        return data

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        user = User.objects.create(
           username = user_data['username'],
           email = user_data['email']

        )

        user.set_password(user_data['password'])
        user.save()
        client = Client.objects.create(user=user, adresse=validated_data['adresse'], telephone=validated_data['telephone'])
        client.save()
        
        return client


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