from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.contrib.auth.decorators import login_required


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

@login_required
def logout_view(request):
    logout(request)
    return redirect('main')
    

class RegisterView(View):
    def get(self, request):
        register_form=UserCreationForm()
        return render(request, "views/register.html", {"register_form":register_form})
    
    def post(self, request):
        register_form=UserCreationForm(data=request.POST)
        if register_form.is_valid():
            user=register_form.save()
            user.refresh_from_db()
            login(request, user)
            messages.success(request, f"user {user.username} registered successfully")
            return redirect ('home')
        else:
            messages.error(request, f'error during register.')
            return render(request, "views/register.html", {"register_form":register_form})
    