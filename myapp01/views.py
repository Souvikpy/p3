from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def trails(request):
    return HttpResponse ("<h1> Project is on air </h1>")

def base(request):
    return render(request,"base.html")

def home(request):
    return render(request,"myapp01/home.html")

def profile(request):
    name="Souvik"
    return render(request,"myapp01/profile.html",{'name':name})