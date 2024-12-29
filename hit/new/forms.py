from django.forms import *
from .models import *

class Bill_Items_Forms(ModelForm):
    class Meta:
        model = Bill_Items
        fields = '__all__'

class Soft_drinks_Forms(ModelForm):
    class Meta:
        model = Soft_drinks
        fields = '__all__'