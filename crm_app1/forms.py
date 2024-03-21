from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CustomerRecord


class CustomerRecordForm(forms.ModelForm):
    class Meta:
        model = CustomerRecord
        fields = "__all__"




class SignupForm(UserCreationForm):
    email = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email','password1','password2')
        