from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def fun1(request):
    return HttpResponse("Haii...")

def fun2(request):
    return HttpResponse("Hello..")

def fun3(req):
    return render(req,'demo.html')

def fun4(req):
    return render(req,'home.html')

def fun5(req):
    return render(req,'contact.html')

def fun6(req):
    return render(req,'about.html')
