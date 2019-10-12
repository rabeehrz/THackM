from django.shortcuts import render
from .models import User

# Create your views here.

def index(request):
    return render(request, 'users/index.html')

def login(request):
    name = request.POST.get('name', "Default")
    person = User.objects.all().filter(name=name)
    context = {
        "name" : name
    }
    return render(request,'users/home.html',context)