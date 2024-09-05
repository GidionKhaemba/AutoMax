from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login


# Create your views here.

def login_view(request):
    if request.method=="POST":        
        login_form=AuthenticationForm(request=request, data=request.POST)
        if login_form.is_valid():
            username=login_form.cleaned_data.get('username')
            password=login_form.cleaned_data.get('password')
            user=authenticate(username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                messages.success(request, f'You have logged in as {username}')
                return redirect('home')
                
        else:
            messages.error(request, f'error occurred trying to log in')
    elif request.method=='GET':
        login_form=AuthenticationForm()       
    context= {"login_form":login_form}
    return render(request,'views/login.html', context)