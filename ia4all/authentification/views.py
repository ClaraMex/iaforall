from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def inscription(request):
    return render(request, "inscription.html")

def connexion(request):
    return render(request, "connexion.html")

def deconnexion(request):
    logout(request)
    return redirect("connexion")

@login_required
def index(request):
    return render(request, "index.html")