from django import forms
from .models import BlogPost, Comment


class EntryForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content']
        labels = {'title': '', 'content': ''}
        widgets = {'content': forms.Textarea(attrs={'cols': 80})}


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        labels = {'comment': ''}
        widgets = {'comment': forms.Textarea(attrs={'cols': 80})}
