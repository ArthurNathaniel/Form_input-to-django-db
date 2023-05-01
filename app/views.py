from app.models import User
from .models import User
from django.shortcuts import render, redirect
from django.shortcuts import render
from .models import User


# Create your views here.


def home(request):
    return render(request, 'home.html')


# views.py


def create_user(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        user = User(name=name, email=email, password=password)
        user.save()
        return redirect('success_page')
    else:
        return render(request, 'create_user.html')


def success_page(request):
    return render(request, 'success_page.html')


def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})
