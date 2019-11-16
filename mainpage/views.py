from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    welcome = {"introduction": "Welcome to my site", "ID": "329085"}
    return render(request, "main.html", welcome)

def additional_view(request, *args, **kwargs):
    text = {"description": "About me:", "ID": "201739"}
    return render(request, "add-on.html", text)

