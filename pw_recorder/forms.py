from django import forms
from .models import App


class AppForm(forms.ModelForm):
    class Meta:
        model = App
        fields = ("name", "password")
        widgets = {
            'name': forms.TextInput(attrs={'id': 'reg', 'name': 'name'}),
            'password': forms.TextInput(attrs={'id': 'reg pw', 'name': 'password'}),
        }