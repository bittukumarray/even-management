from django import forms
from .models import *
from django.core.exceptions import ValidationError
from django.http import HttpResponse


class GuestForm(forms.ModelForm):
    # password = forms.CharField(widget=forms.PasswordInput())
    # confirm_password = forms.CharField(widget = forms.PasswordInput())
    class Meta:
        model = Guest
        fields = ['host','name','email','phone_number']

    
    def __init__(self, *args, **kwargs):
        super(GuestForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
        })

class GuestCheckoutForm(forms.ModelForm):
    # password = forms.CharField(widget=forms.PasswordInput())
    # confirm_password = forms.CharField(widget = forms.PasswordInput())
    class Meta:
        model = Guest
        fields = ['token']

    
    def __init__(self, *args, **kwargs):
        super(GuestCheckoutForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
        })
    


class HostForm(forms.ModelForm):
    class Meta:
        model = Host
        fields = ['name', 'email', 'event_address', 'phone_number',]
    

    def __init__(self, *args, **kwargs):
        super(HostForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
        })