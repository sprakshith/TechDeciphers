from django import forms
from TechDeciphers_News.models import News


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        exclude = ['newsId']
        widgets = {
            'typeOfNews' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'heading' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'miniHeading' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'completeContent' : forms.Textarea(attrs = {'class' : 'form-control', 'rows' : '28'}),
            'postAuthor' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'postPublishDate' : forms.TextInput(attrs = {'class' : 'form-control'})
        }
