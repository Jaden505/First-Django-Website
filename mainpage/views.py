from django.http import HttpResponse
from django.shortcuts import render
from mainpage.models import Fields

# Create your views here.
def home_view(request):
    return render(request, "main.html")

def additional_view(request):
    return render(request, "add-on.html")

