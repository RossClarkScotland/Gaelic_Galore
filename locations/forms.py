from django import forms
from .models import Location


class LocationForm(forms.ModelForm):
    """ allows superusers to add new locations """
    class Meta:
        model = Location
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'rounded-0'
