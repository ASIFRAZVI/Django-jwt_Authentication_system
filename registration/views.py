from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *
from rest_framework.authentication import BaseAuthentication, SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token

class registration_APIView(APIView):
    permission_classes=[AllowAny]
    
    def post(self,request):
        user_serializer=user_registration_serializers(data=request.data)
        password = request.data.get('password')
        request.data['password'] = make_password(password) 

        if user_serializer.is_valid():
            user_serializer.save()
            return Response({'message':'sucussfully user registered' }, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Error while registration', 'errors': user_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class login_user_APIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        login_serializer = login_serializers(data=request.data)

        if login_serializer.is_valid():
            username = login_serializer.validated_data.get('username')
            password = login_serializer.validated_data.get('password')
            # print(username, password)

            try:
                user = Register_user.objects.get(username=username)
            except Register_user.DoesNotExist:
                return Response({'error': 'Invalid username'}, status=status.HTTP_400_BAD_REQUEST)

            if check_password(password, user.password):
                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    'message': 'Login successful, redirecting to dashboard'
                }, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(login_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

      
