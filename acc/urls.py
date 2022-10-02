from django.urls import path
from . import views

app_name = "acc"

urlpatterns = [
    path('index/', views.index, name="index"),
    path('login/', views.userlogin, name="login"),
    path('logout/', views.userlogout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('delete/', views.delete, name="delete"),
    path('signup/', views.signup, name="signup"),
    path('update/', views.update, name="update")
]