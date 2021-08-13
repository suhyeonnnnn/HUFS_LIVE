from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] != request.POST['password2']:
            return render(request, 'signup.html', {'error': '비밀번호가 일치하지 않습니다'})
        else:
            user = User.objects.create_user( username=request.POST['username'], first_name=request.POST['nickname'], password=request.POST['password1'])
            auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('home')
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': '아이디 혹은 비밀번호가 일치하지 않습니다'})
    else:
        return render(request, 'login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return render(request, 'login.html')