from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
  class Meta(UserCreationForm):
    model = CustomUser
    fields = ('username', 'email', 'text', 'picture',)

# class CustomUserChangeForm(UserChangeForm):
#   class Meta(UserChangeForm):
#     model = CustomUser
#     fields = ('email', 'text', 'picture',)

class BioForm(forms.ModelForm):
  class Meta:
    model = CustomUser
    fields = ('email', 'text', 'picture',)