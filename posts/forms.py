from django import forms
from . import models

class CreatePost(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title', 'body', 'slug', 'draft', 'thumb']

class UpdatePost(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title', 'body', 'slug', 'draft', 'thumb']

class CreateComment(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['body', 'post']