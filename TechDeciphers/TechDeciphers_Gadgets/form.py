from django import forms
from TechDeciphers_Gadgets.models import Gadgets


class GadgetForm(forms.ModelForm):
    class Meta:
        model = Gadgets
        exclude = ['gadgetId']
        widgets = {
            'gadgetId' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'typeOfGadget' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'heading' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'miniHeading' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'miniContent' : forms.Textarea(attrs = {'class' : 'form-control', 'rows' : '6'}),
            'completeContent' : forms.Textarea(attrs = {'class' : 'form-control', 'rows' : '28'}),
            'postAuthor' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'postPublishDate' : forms.TextInput(attrs = {'class' : 'form-control'})
        }
