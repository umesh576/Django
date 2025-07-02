from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("hello world thid is home page")
    return render(request, 'website/index.html')

def about(request):
    return HttpResponse("This is about page.")

def contact(request):
    return HttpResponse("This is conatct page")


