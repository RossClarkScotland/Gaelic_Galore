from django import forms
from .models import Order

# as shown in Boutique Ado walkthrough project

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('first_name', 'surname', 'email', 'phone',
                  'address', 'town_or_city', 'postcode', 
                  'country', 'county',)

    def __init__(self, *args, **kwargs):
    # add placeholders + classes, remove auto-generated labels + set autofocus
        super().__init__(*args, **kwargs)
        placeholders = {
            'first_name': 'First Name',
            'surname': 'Surname',
            'email': 'Email Address',
            'phone': 'Phone Number',
            'town_or_city': 'Town or City',
            'address': 'Address',
            'county': 'County',
            'country': 'Country',
            'postcode': 'Postcode',
        }

        self.fields['first_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False