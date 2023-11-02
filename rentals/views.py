from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate ,login ,logout
from django.contrib.auth.decorators import login_required
from .models import * 
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
            return redirect('/'+username)
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
        return redirect('/register/'+username)
    return render(request,'registerpage.html')

# Only User can access (Who authenticated)

def completeregister(request,user):
    name = User.objects.filter(username=user)
    if name :
        if request.method == 'POST':
            name = User.objects.get(username=user)
            if CycleInfo.objects.filter(username = name).exists():
                messages.info(request,'You have already created Your account . You can make changes after login')
                return redirect('/login')
            cycle_desc = request.POST.get('cycle_desc')
            cycle_price = request.POST.get('cycle_price')
            phone_no = request.POST.get('phone_no')
            cycle_image = request.FILES.get('cycle_image')


            CycleInfo.objects.create(
                username = name,
                cycle_details = cycle_desc,
                cycle_pricing = cycle_price,
                cycle_img = cycle_image,
                phone_no = phone_no
            )
            Coins.objects.create(
                username = name,
                coins = 100
            )
            
            messages.info(request,'You have successfully registered ! Login Now')
            return redirect('/login')
        context ={'user':user}
        return render(request,'filldetails.html',context)
    else :
        return render(request,'base.html')    
            
@login_required
def userhome(request,user):
    user1 = User.objects.get(username=user)
    user2 = CycleInfo.objects.get(username=user1)
    user3 = Coins.objects.get(username=user1)

    first_name = user1.first_name
    last_name = user1.last_name
    coins = user3.coins
    cycle_desc = user2.cycle_details
    cycle_price = user2.cycle_pricing
    cycle_image = user2.cycle_img
    phone_no = user2.phone_no
    email = user1.email

    context = {'first_name':first_name,'last_name':last_name,
               'coins':coins, 'cycle_desc':cycle_desc ,'cycle_price':cycle_price
               ,'cycle_image':cycle_image, 'phone_no':phone_no , 'email':email}


    return render(request,'userhome.html',context)
    
@login_required
def logout_(request):
    logout(request)
    return redirect('/login/')