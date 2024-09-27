from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *a, **k):
    print(request.user)
    # return HttpResponse("<hi>Hello World</h1>") # string of html code.
    return render(request, "home.html", {})


def contact_view(request, *a, **k):
    return render(request, "contact.html", {})


def about_view(request, *a, **k):
    my_context = {
        "my_text": "This is about us.",
        "my_number": 69,
        "my_list": [13, 69, 678, 902],
        "this_is": True,
    }
    return render(request, "about.html", my_context)


def social_view(request, *a, **k):
    return render(request, "social.html", {})
