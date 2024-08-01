from django import forms
from .models import Donation, NewsletterSubscription

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['first_name', 'last_name', 'email', 'amount', 'message']

class NewsletterSubscriptionForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscription
        fields = ['email']
