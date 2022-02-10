from email import message
import http
import imp
import re
from django.forms import ValidationError
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import *
from .forms import TaskForm,UpdateForm,UserForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.validators import validate_email

# Create your views here.
def listTask(request):
    # queryset=task.objects.order_by('complete','due')
    queryset=task.objects.order_by('-id')
    # print(queryset)
    form=TaskForm()
    if request.method == 'POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    profile= Profile.objects.get(user=request.user)
    context={'form':form,'listtask':queryset,'profile':profile}
    return render(request,'listtask.html',context)
def updateTask(request,pk):
    print(pk)
    queryset=task.objects.get(id=pk)
    print(queryset)
    form=UpdateForm(instance=queryset)
    # print(form)
    if request.method=='POST':
        form=UpdateForm(request.POST,instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form,'listtask':queryset}
    return render(request,'update_task.html',context)
def deleteTask(request,pk):
    queryset=task.objects.get(id=pk).delete()
    # if request.method == "POST":
    #     queryset.delete()
    return redirect('/')
    # context={'delete_task':queryset}
    # return render(request,'delete_task.html',context)
def sign_in(request):
    if request.method=="POST":
        username=request.POST.get('username')
        userpassword=request.POST.get('password')
        print(username,userpassword)
        user=authenticate(username=username,password=userpassword)
        if user is not None:
            login(request,user)
            messages.success(request,'Successfully logged in')
            return redirect('/')
        else:
            messages.error(request,'Invalid Credentials!!,Please try again')
            return redirect('login')
        
    context={}
    return render(request,'authentication/login.html',context)
def sign_out(request):
    if request.method == "POST":
        logout(request)
        messages.success(request,'Successfully Logout')
        return redirect('login')
    return redirect('/')
def sign_up(request):
    if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        # print(username,userpassword)
        
        if not username.isalnum():
            messages.success(request,'Username character must alpha-numeric')
            return redirect('register')
        if len(username)<5:
            messages.success(request,'Username character must be greater than 5')
            return redirect('register')
       
        try:
            if validate_email(email):
                
                return redirect('register')
        except ValidationError as e:
            messages.success(request,'Please enter correct email')
            return redirect('register')
        if password1!=password2:
            messages.success(request,'Password must be same')
            return redirect('register')
       

        user=User.objects.user = User.objects.create_user(username=username, password=password1,email=email)
        user.save()
        messages.success(request,'Account Created for ' + ' ' + username.title())
        return redirect('/')
    
    
        
    return render(request,'authentication/sign_up.html')
def account(request):
    user= Profile.objects.get(user=request.user)
    form=UserForm(instance=user)
    # print(dir(user))
    print(user.phone)
    print(user.profile_pic)
    # print(user[0])
    # # print(dir(user[0]))
    if request.method=="POST":
        form=UserForm(request.POST,request.FILES,instance=user)
        if form.is_valid():
            form.save()
            return redirect('/')
    
   
    
    context={'form':form,'user':user}
    return render(request,'authentication/profile.html',context)


