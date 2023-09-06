from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated

class UserLogin(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user:
            # User is authenticated, generate and return a token
            token, _ = Token.objects.get_or_create(user=user)
           
            return Response({'token': token.key})
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)





class UserRegistration(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            email = serializer.validated_data['email']

            # Check if the username or email is already in use
            if User.objects.filter(username=username).exists():
                return Response({'message': 'Username already exists.'}, status=status.HTTP_400_BAD_REQUEST)

            if User.objects.filter(email=email).exists():
                return Response({'message': 'Email address already in use.'}, status=status.HTTP_400_BAD_REQUEST)

            # Create a new User
            user = User.objects.create_user(username=username, password=password, email=email)
            
            # Generate and return a token for the user
            token, created = Token.objects.get_or_create(user=user)

            return Response({'message': 'User created successfully.', 'token': token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserDetails(APIView):
    permission_classes = [IsAuthenticated]
  


    def get(self, request):
        user = request.user
        user_data = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            # Add other user attributes you want to include here
        }
        return Response({'user': user_data}, status=status.HTTP_200_OK)