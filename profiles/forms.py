from django import forms
from .models import UserProfile

# as shown in Boutique Ado walkthrough project

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile()
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
    # add placeholders + classes, remove auto-generated labels + set autofocus
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone': 'Phone Number',
            'default_town_or_city': 'Town or City',
            'default_address': 'Address',
            'default_county': 'County',
            'default_postcode': 'Postcode',
        }

        self.fields['default_phone'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].widget.attrs['class'] = 'border-black rounded-0'
                self.fields[field].label = False