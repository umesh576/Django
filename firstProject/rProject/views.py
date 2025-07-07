from django.shortcuts import render
from django.http import HttpResponse
from .models import chaiModel
from django.shortcuts import get_list_or_404
# Create your views here.
def allChai(request):
    chai = chaiModel.objects.all()
    return render(request, 'rProject/all_rProject.html',{'chais':chai})

def chaiDetails(request, chai_id):
    chai = get_list_or_404(chaiModel, pk = chai_id)
    return render(request, 'rProject/chai_details.html',{'chai':chai})
