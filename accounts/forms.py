from django import forms
from .models import Address  # Import your Address model

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['contact_name', 'contact_number', 'address_type', 'street_address', 'pincode', 'city', 'state', 'landmark']
