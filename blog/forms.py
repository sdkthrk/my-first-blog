""" forms.py """
from django import forms

from .models import Post, Comment

class PostForm(forms.ModelForm):
    """name: PostForm """
    class Meta:
        model = Post
        fields = ('title', 'text',)

class CommentForm(forms.ModelForm):
    """name: CommentForm """
    class Meta:
        model = Comment
        fields = ('author', 'text',)
