from django import forms
from students.models import Student
from django.core.exceptions import NON_FIELD_ERRORS


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = '__all__'
        exclude = ('subjects',)
        #fields = ('per_id', 'per_name', 'per_code', 'per_addr', 'per_email', 'joined_date', 'average_score', 'subjects')
        error_messages = {
            'per_code': {
              'unique': ('This field must unique'),
            },
        }