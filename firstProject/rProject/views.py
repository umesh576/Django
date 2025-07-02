from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def allChai(request):
    return render(request, 'rProject/all_rProject.html')
