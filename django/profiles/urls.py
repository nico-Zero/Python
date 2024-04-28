from django.urls import path
from .views import My_profile_view

app_name = "profiles"

urlpatterns = [path("", My_profile_view, name="my")]
