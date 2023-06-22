from django.contrib import messages, auth
from api.models import User
from django.shortcuts import render,redirect


def index(request):
    if request.method == 'POST':
        email = (request.POST['email']).lower()
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            return render(request,'users.html')

        else:
            messages.info(request, "invalid user")
            return redirect("/")
    if request.user.is_authenticated:
        return render(request, 'users.html')
    else:
        return render(request,'index.html')



def register(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = (request.POST['email']).lower()
        email = email.strip()
        pass1 = request.POST['password']
        pass2 = request.POST['repassword']

        if pass1==pass2:
            if User.objects.filter(email = email).exists():
                messages.info(request,'Email Already Taken')
            else:
                user=User.objects.create_user(email=email,password=pass1,first_name = fname,last_name = lname)
                user.save()
                return redirect('/')
        else:
            messages.info(request, 'both password are not save')

    return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')



def profile(request,idd):
    udata =  User.objects.get(id=idd)
    print(idd)
    print(udata.first_name)
    return render(request,'profile.html',{"udata":udata})





