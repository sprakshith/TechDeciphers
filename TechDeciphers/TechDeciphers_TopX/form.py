from django import forms
from TechDeciphers_TopX.models import TopX


class TopXForm(forms.ModelForm):
    class Meta:
        model = TopX
        exclude = ['topXId']
        widgets = {
            'typeOfTopX' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'heading' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'miniHeading' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'completeContent' : forms.Textarea(attrs = {'class' : 'form-control', 'rows' : '28'}),
            'postAuthor' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'postPublishDate' : forms.TextInput(attrs = {'class' : 'form-control'})
        }
