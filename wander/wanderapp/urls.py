from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("appregister", views.appregister, name="appregister"),
    path("applogin", views.applogin, name="applogin"),
    path("applogout", views.logout, name="applogout"),
]