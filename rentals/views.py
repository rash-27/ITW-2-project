from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate ,login ,logout
from django.contrib.auth.decorators import login_required
from .models import * 
from collections import OrderedDict
# Create your views here.
import uuid
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
    username = User.objects.get(username=user)
    user2 = CycleInfo.objects.get(username=username)
    user3 = Coins.objects.get(username=username)

    first_name = username.first_name
    last_name = username.last_name
    coins = user3.coins
    cycle_desc = user2.cycle_details
    cycle_price = user2.cycle_pricing
    cycle_image = user2.cycle_img
    phone_no = user2.phone_no
    rating = format(user2.rating,'1f')
    email = username.email

    context = {'first_name':first_name,'last_name':last_name,'username':user,
               'coins':coins, 'cycle_desc':cycle_desc ,'cycle_price':cycle_price
               ,'cycle_image':cycle_image, 'phone_no':phone_no , 'email':email,'rating':rating}


    return render(request,'userhome.html',context)
    
@login_required
def logout_(request):
    logout(request)
    return redirect('/login/')


@login_required
def bookaride(request,user):
    name = User.objects.get(username=user)
    if request.method == 'POST':
        from_time = request.POST.get('from_time')
        to_time = request.POST.get('to_time')
        address = request.POST.get('address')
        uniq = uuid.uuid4().hex[:6]
        while  Booking.objects.filter(uniq=uniq).exists():
            uniq = uuid.uuid4().hex[:6]
        Booking.objects.create(
            uniq = uniq ,
            username = name,
            from_time = from_time ,
            to_time = to_time ,
            address_at = address ,
        )
        context = {'uniq':uniq,'from_time':from_time,'to_time':to_time,'address':address,'username':user}
        return render(request,'bookaride.html',context)
    uniq = Booking.objects.filter(username=name)
    context = {'username':user}
    
    return render(request,'bookaride.html',context)




@login_required
def rentaride(request,user):
    name = User.objects.get(username=user)
    info = Booking.objects.all()
    context = {'username':user,'info':info}
    if request.method == 'POST':
        uniq = request.POST.get('submit')
        print(uniq)
        name = User.objects.get(username=user)
        if Giving.objects.filter(uniq=uniq,username=name).exists():
            # messages.info(request,'Already a offer is sent to the user')
            print('denied')
            return redirect('/'+user+'/Rent-a-ride',context)
        else:
            Giving.objects.create(
                uniq = uniq,
                username = name
            )
            print('created')
            x = Booking.objects.filter(uniq=uniq)
            return redirect('/'+user+'/Rent-a-ride',context)
    return render(request,'rentaride.html',context)



@login_required
def bookingstatustake(request,user):
    name = User.objects.get(username=user)
    uniq = Booking.objects.filter(username=name)
    context = {'username':user,'uniq':uniq}
    if uniq.exists():
        it = Giving.objects.filter(uniq=uniq[0].uniq)
    else : 
        it = False
    if it and  it.exists():
        context['it']=it  
        context1 = []  
        for i in it : # we will get the user name form here   
            bt1 = User.objects.get(username=i.username)
            bt = CycleInfo.objects.filter(username=bt1)
            context1 += bt
        context['bt']= context1
        print(context['bt'])
    if uniq.exists():
        context['uniq']=uniq[0].uniq
    return render(request,'bookingstatustake.html',context)

@login_required
def bookingstatusgive(request,user):
    x = MutualInfo.objects.filter(username2=user)
    y1 = User.objects.get(username = user)
    y = Giving.objects.filter(username=y1)
    context = {'username':user}
    if y :
        context['y']=y
    if x :
        context['info']=x
        username1 = x[0].username1
        name = User.objects.get(username=username1)
        y = CycleInfo.objects.filter(username=name).values()
        context['user']=name.username
        context['phone_no'] = y[0]
        context['email']=name.email
        context['first_name']= name.first_name
        context['last_name']=name.last_name
    if request.method == 'POST':
        uniq = MutualInfo.objects.filter(username2=user)[0]
        uniq.taken = True
        uniq.delete()
        return redirect('/'+user)
    return render(request,'bookingstatusgive.html',context)

@login_required
def bookingaccept(request,user,username):
    name = User.objects.get(username=user)
    uniq = Booking.objects.filter(username=name)
    # p = MutualInfo.objects.filter(username1=user)
    x = User.objects.get(username=username)
    name1 = CycleInfo.objects.filter(username=x)
    if uniq :
        print(username)
        x = User.objects.get(username=username)
        name1 = CycleInfo.objects.filter(username=x)
        username1 = user
        username2 = username
        from_time = uniq[0].from_time
        to_time = uniq[0].to_time

        Transactions.objects.create(
            uniq=uniq[0].uniq,
            username1 = username1,
            username2 = username2,
            from_time = from_time,
            to_time = to_time
        )


        MutualInfo.objects.create(
            uniq=uniq[0].uniq,
            username1 = username1,
            username2 = username2,
        )
        y = Giving.objects.filter(uniq = uniq[0].uniq)
        y.delete()
        uniq.delete()
        context = {'username':username1,'username1':username2 ,
                'phone_no':name1[0].phone_no,'email':x.email,'cycle_desc':name1[0].cycle_details,
                'cycle_pricing':name1[0].cycle_pricing,'cycle_image':name1[0].cycle_img}
        return render(request,'mutualtake.html',context)
    context = {'username':user,'username1':username,
               'phone_no':name1[0].phone_no,'email':x.email,'cycle_desc':name1[0].cycle_details,
                'cycle_pricing':name1[0].cycle_pricing,'cycle_image':name1[0].cycle_img,'rating':name1[0].rating}
    return render(request,'mutualtake.html',context)
    

@login_required
def review(request,user,username):
    if request.method == 'POST':
        rating = int(request.POST.get('rating'))
        # review = request.POST.get('review')
        price = int(request.POST.get('price'))
        name1 = User.objects.get(username=user)
        name2 = User.objects.get(username = username)
        x1 = Coins.objects.filter(username=name1)[0]
        x2 = Coins.objects.filter(username=name2)[0]
        x1.coins -= int(price)
        x1.save()
        x2.coins += int(price)
        x2.save()
        x = MutualInfo.objects.filter(username1=user)
        uniq = x[0].uniq
        y = Transactions.objects.filter(uniq=uniq)[0]
        y.rating=int(rating)
        y.cost=int(price)
        y.save()
        z = Transactions.objects.filter(username2=username)
        var = 0
        for i in z :
            var+=int(i.rating)
        var /= z.count()
        t = CycleInfo.objects.filter(username=name2)[0]
        t.rating = var
        t.save()
        messages.info(request,'You Transaction and Payment is successful')
        context = {'username':user,'username1':username}
        return redirect('/'+user+'/Book-a-ride/accept/'+username+'/review',context)

    context = {'username':user,'username1':username}

    return render(request,'review.html',context)


@login_required
def seeTransactions(request,user):
    transac = Transactions.objects.filter(username1= user)
    context = {'username':user,'transactions':transac}
    return render(request,'transactions.html',context)

@login_required
def confirm(request,user,username):
    uniq = MutualInfo.objects.filter(username1=user)[0]
    uniq.taken = True
    uniq.save()
    messages.info(request,'Cycle taken')

    return redirect('/'+user+'/Book-a-ride/accept/'+username)

@login_required
def update(request,user):
    context = {'username':user}
    if request.method == 'POST':
        name = User.objects.get(username=user)
        x = CycleInfo.objects.filter(username = name)[0]
        cycle_desc = request.POST.get('cycle_desc')
        cycle_price = request.POST.get('cycle_price')
        phone_no = request.POST.get('phone_no')
        cycle_image = request.FILES.get('cycle_image')
        x.phone_no = phone_no
        x.cycle_image = cycle_image
        x.cycle_price = cycle_price
        x.cycle_desc = cycle_desc
        x.save()
        messages.info(request,'Your account is Successsfully Updated')
        return render('/'+user+'/Update')
    return render(request,'userupdate.html',context)


def custom_404(request,exception):
    return render(request,'error.html',status=404 or 500)


