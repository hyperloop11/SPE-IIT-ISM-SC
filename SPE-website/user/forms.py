from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserSignUpForm(UserCreationForm):
    email = forms.EmailField()
    spe_id = forms.IntegerField(required=False)
    IIT_ISM_registration_number = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ['email', 'spe_id', 'IIT_ISM_registration_number', 'password1', 'password2']