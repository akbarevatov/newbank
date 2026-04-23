from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

# Create your views here.
def my_account(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'accounts/my_account.html', {'user': user})

def login(request):
    if request.user.is_authenticated:
        return redirect('accounts:my_account', username=request.user.username)
    error_message = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            auth_login(request, user)
            return redirect('accounts:my_account', username=username)
        error_message = 'Invalid username or password'
    return render(request, 'accounts/login.html', {'error_message': error_message})

def logout(request):
    auth_logout(request)
    return redirect('accounts:login')

def register(request):
    if request.user.is_authenticated:
        return redirect('accounts:my_account', username=request.user.username)
    error_message = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        if User.objects.filter(username=username).exists():
            error_message = 'Username already exists'
        elif User.objects.filter(email=email).exists():
            error_message = 'Email already exists'
        else:
            user = User.objects.create_user(username=username, password=password, email=email)
            auth_login(request, user)
            return redirect('accounts:my_account', username=username)
    return render(request, 'accounts/register.html', {'error_message': error_message})