from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.home_view, name="home"),
    path("about/", views.about_view, name="about"),
    path("post/<int:pk>/", views.show_post_view, name="show_post"),
    path("edit_post/<int:pk>/", views.edit_post_view, name="edit_post"),
    path("create_post/", views.create_post_view, name="create_post"),
    path("delete_post/<int:pk>/", views.delete_post_view, name='delete_post'),
    path("profile/<int:pk>/", views.profile_view, name="profile"),
    path("edit_profile/",views.edit_profile_view, name="edit_profile"),
    path("login/",views.loginPage_view, name="login"),
    path("register/",views.registerPage_view, name="register"),
    path("logout/",views.logout_view, name="logout"),

]
