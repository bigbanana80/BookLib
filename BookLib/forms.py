from django import forms
from django.core.validators import MinLengthValidator
from .models import GENDERS

class AuthorForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    age = forms.IntegerField()
    national_code = forms.CharField(
        max_length=10, validators=[MinLengthValidator(10)]
    )
    gender = forms.ChoiceField(choices=GENDERS)