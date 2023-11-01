from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate ,login
# Create your views here.

def homepage(request):
    return render(request,'home.html')

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not User.objects.filter(username=username).exists():
            messages.error(request,'Invalid Username')
            return redirect('/login')
        user = authenticate(username=username,password=password)
        if user is None:
            messages.error(request,'Invalid Password')
            return redirect('/login')
        else :
            login(request,user)
            return redirect('/')
    return render(request,'loginpage.html')

def registerpage(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('user_name')
        firstname = request.POST.get('first_name')
        lastname = request.POST.get('last_name')
        password = request.POST.get('password')
        user = User.objects.filter(email=email)
        if user.exists():
            messages.info(request,'This Email is already under use.')
            return redirect('/register')
        user = User.objects.filter(username=username) 
        if user.exists():
            messages.info(request,' Username is not available , Please try another one .')
            context={'username':username}
            return render(request,'registerpage.html',context)
        user = User.objects.create(
            first_name = firstname,
            last_name = lastname,
            username = username,
            email = email
        )
        user.set_password(password)
        user.save()
        messages.info(request,'You have successfully created your account. Now fill the details')
        return redirect('/register')
    return render(request,'registerpage.html')