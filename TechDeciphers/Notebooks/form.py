from django import forms
from Notebooks.models import Notebook

class NotebookForm(forms.ModelForm):
    class Meta:
        model = Notebook
        exclude = ['notebook_id']
        widgets = {
            'heading' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'description' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'content' : forms.Textarea(attrs = {'class' : 'form-control', 'rows' : '28'}),
            'postAuthor' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'postPublishDate' : forms.TextInput(attrs = {'class' : 'form-control form-datepicker'})
        }
