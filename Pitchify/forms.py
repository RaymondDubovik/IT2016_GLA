from django.contrib.auth.models import User
import re
from pitchify.models import Company, Investor, Pitch
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


class PitchForm(forms.ModelForm):
    class Meta:
        model = Pitch
        fields = ('title', 'description', 'price_per_stock', 'total_stocks', 'youtube_video_id')

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('youtube_video_id')

        # If url is not empty and doesn't start with 'http://' add 'http://' to the beginning
        if url and 'youtube' in url:
            # regex for the YouTube ID: "^[^v]+v=(.{11}).*"
            result = re.match('^[^v]+v=(.{11}).*', url)
            url = result.group(1)

            cleaned_data['youtube_video_id'] = url
        return cleaned_data
