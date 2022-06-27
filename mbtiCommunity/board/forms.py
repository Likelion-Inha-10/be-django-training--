from socket import fromshare
from django import forms
from django.forms import widgets
from .models import board

class addPostForm(forms.ModelForm):
    class Meta:
        model = board
        fields = ['title', 'author', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.TextInput(attrs={'class':'form-control'}),
            'content': forms.TextInput(attrs={'class':'form-control'}),
        }