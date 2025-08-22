from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from . forms import UserLoginFrom , UserSignupForm
# Create your views here.

def login_view(request):
    return render(request, 'user_auth/login_page.html')


def logout_view(request):
    return render(request, 'user_auth/logout_page.html')


def login_view(request):
    if request.method == 'POST': # when the form is submitted
        form = UserLoginFrom(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else: # when the page is loaded
        form = UserLoginFrom()
    return render(request, 'user_auth/login_page.html', {'form': form})   
         

def signup_view(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = UserSignupForm()
    return render(request, 'user_auth/signup_page.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect("{% url 'login' %}")