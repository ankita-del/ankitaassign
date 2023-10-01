"i have created website"
from django.shortcuts import render
def login(request):
    return render (request,"login.html")