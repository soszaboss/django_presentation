from django.forms import ModelForm
from .models import Authors, Books
from django import forms


"""Conception de formulaire 
    Django vous permet de concevoir des formulaires en utilisant le module forms,
    et il permet la conception de vos formulaires en fonction de la definition de vos models
    ce qui vous permet de vous concentrez sur votre code
"""


class AuthorsForm(ModelForm):
    class Meta:
        model = Authors
        fields = ['fullname', 'birth_date', 'nationality']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }

class BooksForm(ModelForm):
    class Meta:
        model = Books
        fields = ['title', 'isbn', 'publication_date', 'author']
        widgets = {
            'publication_date': forms.DateInput(attrs={'type': 'date'}),
        }
