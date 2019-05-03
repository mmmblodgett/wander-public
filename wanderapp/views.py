from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.models import User

import googlemaps
GM = googlemaps.Client(key="AIzaSyDWty8o-JfoqiS3iIyMFxt3qcZBc7a9fGo")



# Create your views here.
def index(request):
    context = {}
    return render(request, "wanderapp/index.html", context=context)

def view_user(request, user_id):
    context = {
        "user_id": user_id,
        "username": User.objects.get(pk=user_id).username,
        "my_profile": user_id == request.user.pk,
        "places": None,
        "GM": GM,
    }
    return render(request, "wanderapp/user.html", context=context)


def appregister(request):
    """Render the register page and handle the creation of a new user"""
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
        try:
            user = User.objects.create_user(request.POST["username"], request.POST["email"], request.POST["password"])
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        except:
            return render(request, "wanderapp/register.html", {"message": "Username is already in use"})
    else:
        logout(request)
        return render(request, "wanderapp/register.html", {"message": None})

def applogin(request):
    """Render the login page and handle a user login request"""
    if request.POST:
        # Get username and password
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Log the user in
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "wanderapp/login.html", {"message": "Invalid credentials."})
    else:
        logout(request)
        return render(request, "wanderapp/login.html", {"message": None})

def applogout(request):
    """Log the user out"""
    logout(request)
    return render(request, "wanderapp/login.html", {"message": "Logged out."})