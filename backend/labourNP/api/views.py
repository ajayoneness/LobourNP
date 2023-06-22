from api.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate,logout,login
from .models import User
from rest_framework import generics

class loginuser(APIView):
    #renderer_classes = [UserRenderer]
    def post(self, request, formate=None):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                users = request.user.id
                #user_type = request.user.user_type
                return Response({'msg':'Login Success','user_id':users}, status=status.HTTP_200_OK)
            else:
                return Response({'msg':'Email or Password is not Valid'}, status=status.HTTP_200_OK)
        return Response(serializer.error, status=status.HTTP_404_BAD_REQUEST) #


class register(APIView):
    def post(self, request, formate=None):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'msg':'Register success'},status=status.HTTP_200_OK)
        return Response(serializer.error, status=status.HTTP_404_BAD_REQUEST)


class logoutAPI(APIView):
    def get(self, request):
        try :
            usremail = request.user.email
        except:
            usremail = None
        logout(request)
        return Response({'message': 'Logged out successfully','usrEmail':f'{usremail}'})


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer