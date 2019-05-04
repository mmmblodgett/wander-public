from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.models import User
from .models import UserSettings, Place

import googlemaps
GM = googlemaps.Client(key="AIzaSyDWty8o-JfoqiS3iIyMFxt3qcZBc7a9fGo")

# Create your views here.
def index(request):
    context = {}
    return render(request, "wanderapp/index.html", context=context)

def view_user(request, user_id):
    user = User.objects.get(pk=user_id)
    try:
        new_place = request.session['new']
    except:
        new_place = False
    context = {
        "user_id": user_id,
        "username": user.username,
        "my_profile": user_id == request.user.pk,
        "privacy": user.settings.privacy,
        "places": user.places.all(),
        "new_place": new_place,
    }
    request.session['new'] = False
    return render(request, "wanderapp/user.html", context=context)

@login_required
def delete(request):
    try:
        Place.objects.get(pk=request.POST['place_id']).delete()
    except:
        return HttpResponse("Place does not exist or could not be deleted")
#    return view_user(request, request.user.id)
    return HttpResponseRedirect("user/"+str(request.user.id))

@login_required
def mark(request):
    place = request.POST['searchbox']
    start_date = request.POST['start-time']
    end_date = request.POST['end-time']
    notes = request.POST['notes']

    if place:
        try:
            geocode_result = GM.geocode(place)[0]
        except:
            return HttpResponse(place+" is not a valid place")

        new_place = Place.objects.create(label = geocode_result['formatted_address'],
        lat = geocode_result['geometry']['location']['lat'],
        lng = geocode_result['geometry']['location']['lng'])
        new_place.user.set([User.objects.get(pk=request.user.id)])
    else:
        return HttpResponse("Please input a place")

    if start_date or end_date:
        if not start_date:
            return HttpResponse("Travel time is missing a start date")
        if not end_date:
            return HttpResponse("Travel time is missing an end date")
        if start_date > end_date:
            return HttpResponse("End date must be later than start date")
        new_place.start_date = start_date
        new_place.end_date = end_date

    if notes:
        new_place.notes = notes
    
    new_place.save()
    request.session['new'] = True
    return HttpResponseRedirect("user/"+str(request.user.id))

@login_required
def privacy(request):
    setting = request.POST['setting']
    try:
        user = request.user
        user.settings.privacy = setting
        user.settings.save()
        return HttpResponseRedirect("user/"+str(user.id))
    except Exception as e:
        return HttpResponse("Something went wrong - " + str(e))

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
            # Create user settings object
            UserSettings.objects.create(user=user)
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