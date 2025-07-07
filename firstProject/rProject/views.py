from django.shortcuts import render
from django.http import HttpResponse
from .models import chaiModel

# Create your views here.
def allChai(request):
    chai = chaiModel.objects.all()
    return render(request, 'rProject/all_rProject.html',{'chai':chai})

