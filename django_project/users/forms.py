from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

# Class to create a form for user registration 
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    # Nested namespace for configurations and keeps it in same place
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Class to create a form for user information
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

# Class to create a form for user profile updation
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
