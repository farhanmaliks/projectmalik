from django import forms
from .models import Contacts, Review

class ContactsForm(forms.ModelForm):
    class Meta: 
        model = Contacts
        fields = ['ContactName', 'ContactEmail', 'Message']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['product_id', 'cust_name', 'cust_email', 'cust_review']