from django import forms
from .models import Course


class CourseForm(forms.ModelForm):
# allows superusers to add new courses
    class Meta:
        model = Course
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'rounded-0'