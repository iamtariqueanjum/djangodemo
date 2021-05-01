from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
    #print(args, kwargs)
    #print(request)
    #print(request.user) # incognito - AnonymousUser
    #return HttpResponse("<h1>Hello World</h1>")
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "this is about context text with capfirst filter ",
        "my_num": 10,
        "my_list": [3123, 123, 123123, "tiger", "apple"],
        "my_html": "<h1>This is safe html</h1>"
    }
    return render(request, "about.html", my_context)

def social_view(request, *args, **kwargs):
    return HttpResponse("<h1>Social Page</h1>")
