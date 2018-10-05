from django.forms.models import inlineformset_factory
from django.forms.models import BaseInlineFormSet

class AnotacaoBaseFormset(BaseInlineFormSet):
    pass

anotacao_form = inlineformset_factory(models.Caderno, models.Anotacao, formset=AnotacaoBaseFormset, extra=1)


