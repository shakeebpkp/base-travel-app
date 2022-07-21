from django.contrib import messages, auth
from django.contrib.auth.models import User


# Create your views here.
from django.shortcuts import render, redirect

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not  None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid user")
            return redirect('login')
    return render(request, "login.html")

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['firstname']
        lname = request.POST['secondname']
        email = request.POST['email']
        number = request.POST['number']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username = username).exists():
                messages.info(request, "username already taken")
                return redirect('register')
            elif User.objects.filter(email = email).exists():
                messages.info(request, "email already taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=fname,
                                                last_name=lname)

                user.save()
                return redirect('login')
        else:
            messages.info(request, "password not matched")
            return redirect('register')
        return redirect('/')
    return render(request, "register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')
