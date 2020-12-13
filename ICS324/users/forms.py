from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from KFUPMCollection.models import resource


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class resource(forms.ModelForm):
    class Meta:
        model = resource
        fields = "__all__"