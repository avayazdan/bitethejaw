# from django.shortcuts import render
from rest_framework import generics
# from os import status
# from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveDestroyAPIView
# from rest_framework.views import APIView
# from rest_framework import status
# from rest_framework import Response
from .models import User
from .serializers import UserSerializer, RegisterSerializer
from rest_framework.permissions import AllowAny


class RegisterView(generics.CreateAPIView):
    """
    CreateAPIView ensures only a create operation is possible
    """
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


# class UsersListView(APIView):
#     def post(self, request):
#         serialized_user = UserSerializer(data=request.data)
#         if serialized_user.is.valid.valid():
#             serialized_user.save()
#             return Response(serialized_user.data)
#         return Response(serialized_user.errors, status=status.HTTP_442_UNPROCESSABLE_ENTITY)

#     def get(self, request):
#         users = User.objects.all()
#         serialized_users = PopulatedUserSerializer(users, many=True)
#         return Response(serialized_users.data)


# class UsersDetailView(RetrieveDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = PopulatedUserSerializer

#     def put(self, request, pk):
#         try:
#             users_to_update = Users.objects.get(pk=pk)
#         except User.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#         serialized_user = UserSerializer(users_to_update, data=request.data)
#         if serialized_user.is_valid():
#             serialized_user.save()
#             return Response(serialized_user.data)
#         return Response(serialized_user.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


# # Create your views here.

class UsersListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UsersDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
