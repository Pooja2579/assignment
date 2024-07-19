from django.shortcuts import render

# Create your views here.

from django.contrib.auth import authenticate
from django.db.models import Q
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import User, FriendRequest
from .serializers import UserSerializer, FriendRequestSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.throttling import UserRateThrottle

# class SignUpView(APIView):
#     def post(self, request):
#         email = request.data.get('email')
#         password = request.data.get('password')
#         name = request.data.get('name')
#         if not email or not password or not name:
#             return Response({'error': 'Email, password and name are required'}, status=status.HTTP_400_BAD_REQUEST)
#         if User.objects.filter(email__iexact=email).exists():
#             return Response({'error': 'Email already exists'}, status=status.HTTP_400_BAD_REQUEST)
#         user = User.objects.create_user(email=email, password=password, name=name)
#         return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
class SignUpView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            return Response(UserSerializer(user).data)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class UserSearchView(generics.ListAPIView):
    serializer_class = UserSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        keyword = self.request.query_params.get('q', '')
        return User.objects.filter(Q(email__iexact=keyword) | Q(name__icontains=keyword))

class FriendRequestThrottle(UserRateThrottle):
    rate = '3/minute'

class SendFriendRequestView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    throttle_classes = [FriendRequestThrottle]

    def post(self, request, user_id):
        sender = request.user
        receiver = User.objects.get(id=user_id)
        if FriendRequest.objects.filter(sender=sender, receiver=receiver, status='sent').exists():
            return Response({'error': 'Friend request already sent'}, status=status.HTTP_400_BAD_REQUEST)
        FriendRequest.objects.create(sender=sender, receiver=receiver)
        return Response({'message': 'Friend request sent'}, status=status.HTTP_201_CREATED)

class HandleFriendRequestView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, request_id, action):
        friend_request = FriendRequest.objects.get(id=request_id, receiver=request.user)
        if action == 'accept':
            friend_request.status = 'accepted'
        elif action == 'reject':
            friend_request.status = 'rejected'
        else:
            return Response({'error': 'Invalid action'}, status=status.HTTP_400_BAD_REQUEST)
        friend_request.save()
        return Response({'message': f'Friend request {action}ed'})

class ListFriendsView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(sent_friend_requests__receiver=self.request.user, sent_friend_requests__status='accepted')

class ListPendingFriendRequestsView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FriendRequestSerializer

    def get_queryset(self):
        return FriendRequest.objects.filter(receiver=self.request.user, status='sent')
