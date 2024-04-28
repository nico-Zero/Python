from django.urls import path
from . import views

urlpatterns = [
    # login section of urls
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("register/", views.registerUser, name="register"),
    
    # Home section of urls
    path("", views.home, name="home"),
    path("room/<int:pk>/", views.room, name="room"),

    # Inside Rooms section of urls
    path("create-room/", views.createRoom, name="create-room"),
    path("update-room/<int:pk>", views.updateRoom, name="update-room"),
    path("delete-room/<int:pk>", views.deleteRoom, name="delete-room"),
]
