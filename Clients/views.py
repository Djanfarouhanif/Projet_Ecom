from django.shortcuts import render
from rest_framework import viewsets, status
from serializers.Clients import UserSerializer, LoginSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Client 


class ClientViewset(viewsets.ModelViewSet):

    queryset = Client.objects.all()
    serializer_class = UserSerializer

class LoginViewset(viewsets.ViewSet):
    permission_classes = [AllowAny]
    
    def create(self, request):
        serializer = LoginSerializer(data=request.data)

       
        if serializer.is_valid():
            user = serializer.validated_data['user']
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            
            return Response({
                "refresh": str(refresh),
                'access': access_token
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



