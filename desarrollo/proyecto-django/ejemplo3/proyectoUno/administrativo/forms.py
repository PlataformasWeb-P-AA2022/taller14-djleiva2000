from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django import forms

from administrativo.models import Propietario, Departamento

class PropietarioForm(ModelForm):
    class Meta:
        model = Propietario
        fields = ['nombre', 'apellido', 'edad', 'nacionalidad']
        labels = {
            'nombre': _('Ingrese nombre por favor'),
            'apellido': _('Ingrese apellido por favor'),
            'edad': _('Ingrese su edad por favor'),
            'nacionalidad': _('Ingrese su nacionalidad por favor'),
        }




class DepartamentoForm(ModelForm):
    class Meta:
        model = Departamento
        fields = ['costo_depar', 'num_cuartos', 'num_baños', 'valor_alicuota']



class PropietarioDepartamentoForm(ModelForm):

    def __init__(self, propietario, *args, **kwargs):
        super(PropietarioDepartamentoForm, self).__init__(*args, **kwargs)
        self.initial['propietario'] = propietario
        self.fields["propietario"].widget = forms.widgets.HiddenInput()
        print(propietario)

    class Meta:
        model = Departamento
        fields = ['costo_depar', 'num_cuartos', 'num_baños', 'valor_alicuota']