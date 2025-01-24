from django.shortcuts import render
from django.http import HttpResponse

def nav(request):
    return render(request,"nav.html")
def home(request):
    return render(request,"pages/home.html")
def form(request):
    return render(request,"pages/sam.html")
