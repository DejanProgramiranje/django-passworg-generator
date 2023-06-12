from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.


def home(request):
    return render(request, "generator/home.html")


def password(request):

    thepassword = ""

    characters = list("abcdefgijklmnopqrstuvwxyz")

    # For example, consider the URL https://example.com/search?q=apple&type=fruit.
    # Using request.GET.get("q") would give you the value "apple", and request.GET.get("type")
    # would give you "fruit".
    if request.GET.get("uppercase"):
        characters.extend(list("ABCDEFGHLMNOPQWRSTUVWXYZ"))

    if request.GET.get("special"):
        characters.extend(list("!@#$%^&*()"))

    if request.GET.get("numbers"):
        characters.extend(list("0123456789"))

    length = int(request.GET.get("length", 13))

    for i in range(length):
        thepassword += random.choice(characters)

    return render(request, "generator/password.html", {"password": thepassword})


def about(request):
    return render(request, "generator/about.html")
