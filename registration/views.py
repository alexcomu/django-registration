from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'registration/index.html')

def post(request):
    print dir(request)
    print request.POST['email']
    print request.POST['username']
    print request.POST['password']
    print request.POST['password_repeat']
    return HttpResponse("Hello, world. You're at the register index.")