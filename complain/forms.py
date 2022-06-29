from setuptools import Require
from .models import Complain, Bug
from django import forms



class ComplainForm(forms.ModelForm):
    class Meta:
        model=Complain
        fields = '__all__'
        labels={
            'title':'',
            'body':'',
            'person':'',
        }
        widgets = {
            'person':forms.RadioSelect,
        }
        
    
       

class BugForm(forms.ModelForm):
    class Meta:
        model=Bug
        fields = '__all__'
        widgets={
            'Report':forms.Textarea(attrs={'class':'form-field'})
            }