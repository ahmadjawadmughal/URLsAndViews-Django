from django.urls import path
from urlapp.views import *

urlpatterns = [

    path("home/", home, name="home"),
    path("/about/", about, name="about"),
    path("/profile/<str:username>/", user_profile, name="user_profile"),
    path("/profile_redirect/", profile_redirect, name="profile_redirect"),
]