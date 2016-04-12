# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from django.contrib.auth import authenticate
from django.conf import settings
from models import *

class AutenticationUserForm(forms.Form):
    """ Form used to authenticate users """
    username = forms.CharField(
        label=u'Username',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder': 'Username',
                'required':'',
                'data-error':'Invalid username/password'
            }
        )
    )
    password = forms.CharField(
        label=u'Password',
        widget=forms.PasswordInput(
            render_value=False,
            attrs={'class':'form-control',
            'placeholder': 'Password',
            }
        )
    )

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)


        if not username and not password:
            msg = u'Username and Password fields are required'
            raise forms.ValidationError(msg)

        return self.cleaned_data


class UserForm(ModelForm):

    is_active = models.BooleanField(default=True)

    """UserForm description"""
    class Meta:
        model = User
        fields = ('password','username','email','firstname','lastname')
        widgets = {
            'password':forms.PasswordInput(attrs={'class':'form-control','title':'At least 8 characters','placeholder':'Password'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'username@domain.com','required':'',}),
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Username','required':''}),
            'firstname':forms.TextInput(attrs={'class':'form-control','placeholder':'Firstname','required':''}),
            'lastname':forms.TextInput(attrs={'class':'form-control','placeholder':'Lastname','required':''}),
        }

    def clean_password(self):
        data=self.cleaned_data['password']
        if len(data) < 8:
            raise forms.ValidationError(u"Password must have at least 8 characters")
        if not data :
            raise forms.ValidationError(u"Password is required")
        return data

