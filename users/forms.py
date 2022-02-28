#Django
from django import forms

#Local
from .models import Client

class SignupForm(forms.Form):
    """ Create the signup form """
    first_name =                forms.CharField(max_length=150, min_length=1)
    last_name =                 forms.CharField(max_length=150, min_length=1)
    email =                     forms.EmailField(min_length=1, max_length=50)
    document =                  forms.CharField(max_length=10)
    password =                  forms.CharField(max_length=70, widget=forms.PasswordInput())
    password_confirmation =     forms.CharField(max_length=70, widget=forms.PasswordInput())

    def clean_email(self):
        """ Email must be unique """

        email = self.cleaned_data['email']
        email_taken = Client.objects.filter(email=email).exists()
        if email_taken:
            raise forms.ValidationError('Email is already in use.')
        return email

    def clean(self):
        """Verify password confirmation match"""

        data = super().clean()
        password = data['password']
        password_confirmation = data['password_confirmation']
        if password != password_confirmation:
            raise forms.ValidationError('Passwords do not match.')
        return data

    def save(self):
        """Create new client"""
        
        data=self.cleaned_data
        data.pop('password_confirmation')
        Client.objects.create_user(**data)