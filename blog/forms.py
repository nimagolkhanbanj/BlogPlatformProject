from django import forms
from .models import Post, Category


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category']


class CommentForm(forms.Form):
    content = forms.CharField(max_length=500)