from django import forms
from django.core.exceptions import ValidationError

from .models import Autor


class FormularioAutor(forms.ModelForm):

    fields = ['nome', 'sobrenome']

    class Meta:
        model = Autor