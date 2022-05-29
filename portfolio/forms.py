from django.forms import ModelForm, TextInput
from django import forms
from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
