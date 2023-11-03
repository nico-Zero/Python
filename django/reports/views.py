from django.shortcuts import render
from profiles.models import Profile
from django.http import JsonResponse
from .utils import get_report_image
from .models import Report

# Create your views here.


def is_ajax(request):
    return request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest"


def create_report_view(request):
    if is_ajax(request):
        name = request.POST.get("name")
        remarks = request.POST.get("remarks")
        image = get_report_image(request.POST.get("image"))

        author = Profile.objects.get(user=request.user)
        Report.objects.create(name=name, remarks=remarks, image=image, author=author)
        
        # 4:28:41 in video before. 

        return JsonResponse({"msg": "send"})
    return JsonResponse({})