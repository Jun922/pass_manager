from django import forms
from .models import App


class AppForm(forms.ModelForm):
    class Meta:
        model = App
        fields = ("site_name", "password")
        widgets = {
            'site_name': forms.TextInput(attrs={'id': 'reg', 'name': 'site_name'}),
            'password': forms.TextInput(attrs={'id': 'reg pw', 'name': 'password'}),
        }