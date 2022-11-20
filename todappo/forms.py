from django import forms
from .models import Todo

class TodoForm(forms.Form):
    text = forms.CharField(max_length=255)
    