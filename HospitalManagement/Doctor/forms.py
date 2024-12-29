from django import forms
from .models import *

class Patient_forms(forms.ModelForm):
    
    class Meta:
        model = hospital
        fields = "__all__"
