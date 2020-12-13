from django import forms

class file_form(forms.Form):
    name = forms.CharField()
    Type = forms.CharField()
    file = forms.FileField()
