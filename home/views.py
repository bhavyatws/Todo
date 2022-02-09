import http
import re
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import *
from .forms import TaskForm,UpdateForm

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
    context={'form':form,'listtask':queryset}
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

