
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="home"),
    path('register/', views.register, name="register"),
    path('logout/', views.logout, name="logout"),
    path('profile/<int:idd>/', views.profile, name='profile'),
]
