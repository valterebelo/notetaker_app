from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Note

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()  # Optionally add an email field

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['theme', 'text']  # or any other fields you want to include
