from django.contrib.auth.forms import UserCreationForm
from django import forms
from app.models import *


class BrushForm(forms.ModelForm):
    class Meta:
        model = Brush
        fields = ('owner', 'owner_name')
        labels = {
            'owner': 'صاحب',
            'owner_name': 'نام صاحب',
        }


class PasteForm(forms.ModelForm):
    class Meta:
        model = Paste
        fields = ('level',)
        labels = {
            'level': 'میزان'
        }


class MagicCodeForm(forms.ModelForm):
    class Meta:
        model = MagicCode
        fields = ('user',)
        labels = {
            'user': 'کاربر'
        }

class RegisterForm(UserCreationForm):
   class Meta:
       model = User
       fields = ['username','password1', 'password2']
       labels={
           "username": "نام کاربری",
       }