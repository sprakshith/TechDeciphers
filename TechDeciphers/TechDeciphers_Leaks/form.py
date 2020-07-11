from django import forms
from TechDeciphers_Leaks.models import Leaks

class LeaksForm(forms.ModelForm):
    class Meta:
        model = Leaks
        exclude = ['leakId']
        widgets = {
            'typeOfLeak' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'heading' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'miniHeading' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'completeContent' : forms.Textarea(attrs = {'class' : 'form-control', 'rows' : '28'}),
            'postAuthor' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'postPublishDate' : forms.TextInput(attrs = {'class' : 'form-control'})
        }
