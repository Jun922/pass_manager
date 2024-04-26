from django import forms
from .models import CustomUser

class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)


    class Meta:
        model = CustomUser
        fields = ('nickname',)