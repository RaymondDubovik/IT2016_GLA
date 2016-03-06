from django.contrib.auth.models import User

from pitchify.models import Company, Investor
from django import forms


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    CHOICES = (
        ('', 'Choose a type'),
        ('C', 'Company'),
        ('I', 'Investor')
    )
    type = forms.ChoiceField(choices=CHOICES, required=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'type')



class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('description',)


class InvestorForm(forms.ModelForm):
    class Meta:
        model = Investor
        fields = ('website', 'picture')
