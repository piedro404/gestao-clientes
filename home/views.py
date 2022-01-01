from django.shortcuts import render, redirect
from django.contrib.auth import logout

def home(reguest):
    return render(reguest, "home.html")

def my_logout(reguest):
    logout(reguest)
    return redirect("home")