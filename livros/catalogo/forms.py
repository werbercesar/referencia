from django import forms
from django.core.exceptions import ValidationError

from .models import Papel


class FormPapel(forms.ModelForm):

    fields = ['nome', 'abreviatura', 'autoridade_fonte']

    class Meta:
        model = Papel