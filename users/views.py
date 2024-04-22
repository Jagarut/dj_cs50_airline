from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    print('vamos:', request.user)
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))
    print('index')
    return render(request, 'users/user.html')
    
def login_view(request):
    if request.method == 'POST':
        # print(request.POST)
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            print('dentro')
            login(request, user)
            return HttpResponseRedirect(reverse('users:index'))
        else:
            return render(request, "users/login.html", {'message': 'Invalid credentials.'} )
    return render(request, "users/login.html")

def logout_view(request):
    logout(request)
    return render(request, 'users/login.html', {'message': 'Logged Out'})