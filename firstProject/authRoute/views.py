from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, "website/login.html")

def signUp(request):
    return render(request, "website/signup.html")
def home(request):
    return render(request, "website/home.html")