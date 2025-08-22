from django.shortcuts import render

# Create your views here.

def login_view(request):
    return render(request, 'base/login_page.html')


def logout_view(request):
    return render(request, 'base/logout_page.html')

def signup_view(request):
    return render(request, 'base/signup_page.html')