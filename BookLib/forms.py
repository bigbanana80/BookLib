from django import forms
from .models import Author, Book
    
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["first_name", "last_name", "age", "national_code", "gender"]
        
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["name", "date_published"]