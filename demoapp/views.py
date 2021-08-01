from django.db import models
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from .  import models

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user.is_superuser:
            # login(request, user)
            print("successfully login")
            return HttpResponseRedirect('/timings')
    return render(request,'index.html')

def employeelogin(request):
    if request.method == 'POST':
        print("xxxxxxxxxx")
        username=request.POST['username']
        password=request.POST['password']
        user =models.employee.objects.filter(username=username, password=password).count()
        # user2=models.employee.objects.filter(user_id=user.id)
        if user>0:
            request.session['username']='username'
            request.session['password']='password'
            print("successfully login")
            return HttpResponseRedirect('/timings',{'obj':user})
    return render(request,'employeelogin.html')



def timings(request):
    obj=models.morning.objects.all()
    obj2=models.afternoon.objects.all()
    obj3=models.evening.objects.all()
    return render(request,'timings.html',{'obj':obj,'obj2':obj2,'obj3':obj3})



def morning(request,id):
    mor=models.morning.objects.get(id=id)
    mor.occupied = True
    mor.save()
    return HttpResponseRedirect('/timings')


def afternoon(request,id):
    aft=models.afternoon.objects.get(id=id)
    aft.occupied = True
    aft.save()
    return HttpResponseRedirect('/timings')


def evening(request,id):
    eve=models.evening.objects.get(id=id)
    eve.occupied = True
    eve.save()
    return HttpResponseRedirect('/timings')