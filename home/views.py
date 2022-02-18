
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
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login')
def listTask(request):
    # queryset=task.objects.order_by('complete','due')
    queryset=task.objects.filter(owner=request.user)

    form=TaskForm()
    owner=request.user
    if request.method == 'POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)#it does not save to db                                                             
            obj.owner = owner
            obj.save()

        return redirect('/')
    profile= Profile.objects.get(user=request.user)
    context={'form':form,'listtask':queryset,'profile':profile}
    return render(request,'listtask.html',context)
@login_required(login_url='/login')
def updateTask(request,pk):
    queryset=task.objects.filter(id=pk)
    if queryset.exists():
        queryset=task.objects.get(id=pk)
        form=UpdateForm(instance=queryset)
    # print(form)
        if request.method=='POST':
            form=UpdateForm(request.POST,instance=queryset)
            if form.is_valid():
                form.save()
                return redirect('/')
        context={'form':form,'listtask':queryset}
        return render(request,'update_task.html',context)
    else:
        return redirect('/')
   
@login_required(login_url='/login')
def deleteTask(request,pk):
    queryset=task.objects.filter(id=pk)
    if queryset.exists():
        if request.method == "POST":
            queryset=task.objects.get(id=pk)
            queryset.delete()
            return redirect('/')
            
        else:
            context={'pk':pk} 
            return render(request,'delete_task.html',context)
        
    else:
        return redirect('/')
    

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
                pass
        except ValidationError as e:
            messages.success(request,'Please enter correct email')
            return redirect('register')
        if password1!=password2:
            messages.success(request,'Password must be same')
            return redirect('register')
       

        user=User.objects.create_user(username=username, password=password1,email=email)
        user.save()
        # profile_obj=Profile(user=user)
        # profile_obj.save()
        messages.success(request,'Account Created for ' + ' ' + username.title())
        return redirect('/login')
        
    
    
        
    return render(request,'authentication/sign_up.html')
@login_required(login_url='/login')
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

# def unlock(request):
#     m = User.objects.get(username=request.POST['username'])
#     print(m)
#     if m.check_password(request.POST['password']):
#         request.session['member_id'] = m.id
#         return redirect('/')
#     else:
#         return HttpResponse("Your username and password didn't match.")
# def lock(request):
#     try:
#         del request.session['member_id']
#     except KeyError:
#         pass
#     return HttpResponse("You're logged out.")


