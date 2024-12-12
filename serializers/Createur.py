from rest_framework import serializers
from Createur.models import Createur
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidatonError

MIN_LENGTH = 8

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=MIN_LENGTH, error_messages={"min_length": f"Password must be longer than {MIN_LENGTH} characters"})
    password2 = serializers.CharFiedl(write_only=True, min_length=MIN_LENGTH, error_messages={"min_length": f"Password must be longer than {MIN_LENGTH} characters"})

    class Meta:
        model = User
        fields = ["username", "email" ,"password", "password2"]


class CreateurSerializer(serializers.ModelSerialier):
    user = UserSerializer()

    class Meta:
        model = Createur
        fields = [ "user" ,"contact"] 

    def validate(self, data):
        if data['user']['password'] != data['user']['password2']:
            raise serializers.ValidationError("Password not matching ")

        return data

    def create(self, validated_data):
        user = User.objects.create(username = validated_data['user']['username'], email=validated_data['user']['email'])
        user.set_password(validated_data['user']['password'])
        user.save()

        createur = Createur.objects.create(user=user, contact=validated_data["contact"])



