from django.urls import path
from .views import register,loginuser,logoutAPI,UserDetailAPIView,UserListAPIView

urlpatterns = [
    path('register/', register.as_view(), name='register'),
    path('login/', loginuser.as_view(), name='login'),
    path('logout/',logoutAPI.as_view(), name='logout'),
    path('users/', UserListAPIView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailAPIView.as_view(), name='user-detail'),

]