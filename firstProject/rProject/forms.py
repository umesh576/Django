from django import forms
from .models import chaiModel

class chaiVarietyForm(forms.Form):
    chai_variety = forms.ModelChoiceField(queryset=chaiModel.objects.all(), label="select chai variety:")
