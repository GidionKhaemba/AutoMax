from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Listing

@login_required
def home_view(request):
    listings=Listing.objects.all()
    context={"listings":listings}
    return render(request, 'views/home.html', context)


def main_view(request):
    introduce = "AutoMax"
    return render(request, "views\main.html", {"introduce":introduce})

@login_required
def list_view(request):
    if request.method=="POST":
        pass
    elif request.method=="GET":
        context={}
        return render(request, "views/list.html", context)


