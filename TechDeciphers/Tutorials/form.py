from django import forms
from Tutorials.models import Tutorial

class TutorialForm(forms.ModelForm):
    class Meta:
        model = Tutorial
        exclude = ['tutorial_id']
        widgets = {
            'heading' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'description' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'content' : forms.Textarea(attrs = {'class' : 'form-control', 'rows' : '28'}),
            'postAuthor' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'postPublishDate' : forms.TextInput(attrs = {'class' : 'form-control'})
        }
