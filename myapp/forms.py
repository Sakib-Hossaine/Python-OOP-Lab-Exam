from django.forms import ModelForm
from .models import *

class HospitalForm(ModelForm):
   class Meta:
       model = Hospital
       fields = '__all__'