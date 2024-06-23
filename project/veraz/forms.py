from django import forms
from .models import Formulario

class FormularioForm(forms.ModelForm):
    class Meta:
        model = Formulario
        fields = ['nombre', 'apellido']

from django import forms
from .models import Datos

from django import forms
from .models import Datos

class DatosForm(forms.ModelForm):
    class Meta:
        model = Datos
        fields = ['nombre', 'apellido', 'email', 'direccion', 'archivo', 'numero_gestion']
        labels = {
            'archivo': 'Sube tu archivo:',
        }
        help_texts = {
            'archivo': 'Suba DNI frente y dorso y LIBRE DEUDA DE LA EMPRESA si lo posee',
        }
class FormularioHistorial(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100)
    apellido = forms.CharField(label='Apellido', max_length=100)
    cuil = forms.CharField(label='CUIL', max_length=11)