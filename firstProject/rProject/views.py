from django.shortcuts import render
from django.http import HttpResponse
from .models import chaiModel, Store
from django.shortcuts import get_list_or_404
from .forms import chaiVarietyForm
# Create your views here.
def allChai(request):
    chai = chaiModel.objects.all()
    return render(request, 'rProject/all_rProject.html',{'chais':chai})

def chaiDetails(request, chai_id):
    chai = get_list_or_404(chaiModel, pk = chai_id)
    return render(request, 'rProject/chai_details.html',{'chai':chai})

def chai_store_view(request):
    store = None
    if request.method == 'POST':
        form = chaiVarietyForm(request.POST)
        if form.is_valid():
            chai_variety = form.cleaned_data['chai_variety']
            store = Store.objects.filter(chai_varities = chai_variety)       
    else:
        form = chaiVarietyForm() 

    return render(request, 'rProject/chai_stores.html',{'stores':store,'form':form})
