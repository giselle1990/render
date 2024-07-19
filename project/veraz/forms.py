from django import forms
from .models import Formulario, Datos, RegistroHistorial

class VerazForm(forms.Form):
    OPCIONES = [
        (1, 'Tengo deuda de préstamos de hace 5 años o más'),
        (2, 'Tengo deuda de préstamos de menos de 5 años'),
        (3, 'Tengo deuda de tarjeta de crédito de hace 3 años o más'),
        (4, 'Tengo deuda de tarjeta de crédito de menos de 3 años'),
    ]
    opcion = forms.ChoiceField(choices=OPCIONES, widget=forms.RadioSelect, label='Seleccione una opción')

class NombreApellidoTelefonoCUILForm(forms.Form):
    nombre = forms.CharField(max_length=100, label='Nombre')
    apellido = forms.CharField(max_length=100, label='Apellido')
    telefono = forms.CharField(max_length=20, label='Teléfono')
    cuil = forms.CharField(max_length=20, label='CUIL')



class HistorialForm(forms.ModelForm):
    class Meta:
        model = RegistroHistorial
        fields = ['nombre', 'apellido', 'cuil']
