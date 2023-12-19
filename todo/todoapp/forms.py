from . models import Todotable
from django import forms

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todotable 
        fields = ['name','priority','date']