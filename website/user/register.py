from django import  forms
from  .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class Register(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class Pic_Update(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

class User_Update(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields =['username','email']