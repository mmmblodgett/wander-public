from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.models import User



# Create your views here.
def index(request):
    context = {}
    return render(request, "wanderapp/index.html", context)

def appregister(request):
    if request.POST:
            # Verify inputs
        if not request.POST["username"]:
            return render(request, "wanderapp/register.html", {"message": "No username entered"})
        if not request.POST["email"]:
            return render(request, "wanderapp/register.html", {"message": "No email entered"})
        if not request.POST["password"]:
            return render(request, "wanderapp/register.html", {"message": "No password entered"})
        if request.POST["password"] != request.POST["confirmation"]:
            return render(request, "wanderapp/register.html", {"message": "Passwords do not match"})

        # Create a new user
#        try:
        user = User.objects.create_user(request.POST["username"], request.POST["email"], request.POST["password"])
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
#        except:
#            return render(request, "wanderapp/register.html", {"message": "Username is already in use"})
    else:
        logout(request)
        return render(request, "wanderapp/register.html", {"message": None})

def applogin(request):
    pass

def applogout(request):
        pass