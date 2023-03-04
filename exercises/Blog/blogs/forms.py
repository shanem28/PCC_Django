from django import forms
from .models import BlogPost


class EntryForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content']
        labels = {'title': '', 'content': ''}
        widgets = {'content': forms.Textarea(attrs={'cols': 80})}
