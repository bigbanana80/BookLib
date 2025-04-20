from django.db import models
from django.core.validators import MinLengthValidator

GENDERS = (("1", "MALE"), ("2", "FEMALE"))


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    national_code = models.CharField(
        max_length=10, validators=[MinLengthValidator(10)], unique=True
    )
    gender = models.CharField(max_length=10, choices=GENDERS)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def add_book(self, name, date_published):
        book = Book.objects.create()
        book.name = name
        book.date_published = date_published
        book.author = self
        book.save()


class Book(models.Model):
    name = models.CharField(max_length=300)
    date_published = models.DateTimeField()
    date_creation = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Author, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
