from django.shortcuts import render
from rest_framework import viewsets, status
from serializers.Clients import UserSerializer, LoginSerializer, ClientSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Client 


class ClientViewset(viewsets.ModelViewSet):

    queryset = Client.objects.all()
    serializer_class = ClientSerializer

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

class LogoutViewset(viewsets.ViewSet):

    permission_classes = [IsAuthenticated]

    def create(self, request):
        try:

            # Récupérer le token de rafraîchissement à partir de la requête
            refresh_token = request.data.get('refresh', None)

            if refresh_token:
                # Désactiver le token de rafraîshissement 
                token = RefreshToken(refresh_token)
                token.blacklist() # Si simpleJWT est configuiré dans setting    

                return Response({"message": "Déconnexion réussi "}, status=status.HTTP_200_OK)

        except Exception as e: 
            return Response({'détail': str(e)}, status=status.HTTP_400_BAD_REQUEST)