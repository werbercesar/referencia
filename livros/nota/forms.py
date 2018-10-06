from django.forms.models import inlineformset_factory
from django.forms.models import BaseInlineFormSet
from models import Caderno
from models import Anotacao
from models import Etiqueta


EtiquetaFormset = inlineformset_factory(Anotacao, Etiqueta, Extra=1)

class AnotacaoBaseFormset(BaseInlineFormSet):

    def add_fields(self, form, index):
        super(AnotacaoBaseFormset, self).add_fields(form, index)
        form.nested = EtiquetaFormset(
            instance=form.instance,
            data=form.data if form.is_bound else None,
            files=form.files if form.is_bound else None,
            prefix='etiqueta-%s-%s' % (form.prefix, EtiquetaFormset.get_default_prefix()),
            extra=1
        )

anotacao_form = inlineformset_factory(Caderno, Anotacao, formset=AnotacaoBaseFormset, extra=1)


