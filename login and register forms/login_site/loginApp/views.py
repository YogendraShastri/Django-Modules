from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    return render(request, 'index.html')


def registerpage(request):
    return render(request, 'register.html')

def loginpage(request):
    return render(request, 'login.html')

def handlelogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['userpass1']
        print("username= "+ str(loginusername)+" password = "+ str(loginpassword))

        #authenticate the user if it is user or not in db:
        user = authenticate(username=loginusername,password=loginpassword)
        print(user)
        if user is not None:
            login(request,user)
            messages.success(request, "successfully logged in")
            return redirect('/')
        else:
            messages.error(request, "please enter Valid Credentials")
            return redirect('/')
    


def handlesignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        Email = request.POST['useremail']
        Password = request.POST['userpass1']
        confirmPassword = request.POST['userpass2']
        Address = request.POST['useraddress']

        #uservaliadtion
        if len(username) > 20 or len(username) < 1:
            messages.error(request, "invalid username")
        
        if Password != confirmPassword:
            messages.error(request, "Password does not match")

        #user creation
        createuser = User.objects.create_user(username,Email,Password)
        createuser.Address =  Address
        createuser.save()
        messages.success(request,"Your Registration Completed Successfully")
        
        return redirect('/')
    return HttpResponse('You Need to Login, So Direct Passway')



def handlelogout(request):
    print('i am here bro at logout page')
    if request.method == 'POST':
        print('logout initiating.............')
        logout(request)
        messages.success(request, 'You are successfully logged Out')
        return redirect('/')
    return HttpResponse('logout Done')


