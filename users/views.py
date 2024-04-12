from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from users.forms import CreateUserForm, LoginForm


def members(request):
    return JsonResponse({'hola': 'perro'})

# Create your views here.

def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        
        form = CreateUserForm(request.POST)
        
        if form.is_valid():
            
            form.save()
            
            return redirect('login')
        
    context = {'registerform': form}
    
    return render(request, 'register/register.html', context)

def login(request):
    
    form = LoginForm()
    
    if request.method == 'POST':
        
        form = LoginForm(request, data=request.POST)
        
        if form.is_valid():
            
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)

            if user is not None:
                
                auth.login(request, user)
                
                return redirect("index")
    
    context = {'loginform': form}
    
    return render(request, 'login/login.html', context=context)
            