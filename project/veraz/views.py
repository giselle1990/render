from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FormularioForm, DatosForm, FormularioHistorial
from .models import Formulario, Datos, RegistroHistorial
from .utils import generar_numero_gestion
import logging

logger = logging.getLogger(__name__)

def index(request, numero_gestion=None):
    if request.method == 'POST':
        form = FormularioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            numero_gestion = generar_numero_gestion()
            return render(request, 'veraz/index.html', {'exito': True, 'numero_gestion': numero_gestion})
    else:
        form = FormularioForm()
    
    return render(request, 'veraz/index.html', {'form': form, 'numero_gestion': numero_gestion})

def verificar_supresion_de_datos(request):
    if request.method == 'POST':
        form = DatosForm(request.POST, request.FILES)
        if form.is_valid():
            # Verificar la condición específica
            if not condicion_valida(form.cleaned_data):  # Cambia 'condicion_valida' por tu propia condición
                messages.error(request, 'No puede iniciar el trámite debido a [razón específica].')
                return render(request, 'veraz/formulario.html', {'form': form})

            # Generar el número de gestión
            numero_gestion = generar_numero_gestion()

            # Guardar el número de gestión junto con otros datos en la base de datos
            datos = form.save(commit=False)
            datos.numero_gestion = numero_gestion
            datos.save()

            logger.debug("Procesamiento exitoso del formulario DatosForm.")
            # Redirigir al usuario al inicio
            return redirect('index')
    else:
        form = DatosForm()
    
    return render(request, 'veraz/formulario.html', {'form': form})

def condicion_valida(data):
    # Implementa aquí tu lógica de verificación
    # Devuelve True si la condición se cumple, False en caso contrario
    # Ejemplo de lógica, reemplázala con tu propia lógica
    if data.get('campo_especifico') == 'valor_esperado':
        return True
    return False

def historial(request):
    if request.method == 'POST':
        form = FormularioHistorial(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            cuil = form.cleaned_data['cuil']

            # Guardar datos en la base de datos
            registro = RegistroHistorial(nombre=nombre, apellido=apellido, cuil=cuil)
            registro.save()

            # Mostrar un mensaje
            messages.success(request, 'Datos guardados exitosamente.')

            # Redirigir al usuario al índice
            return redirect('index')
    else:
        form = FormularioHistorial()

    return render(request, 'veraz/historial.html', {'form': form})

def datos_view(request):
    if request.method == 'POST':
        form = DatosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirige a la página de inicio después de guardar los datos
    else:
        form = DatosForm()
    
    return render(request, 'datos_form.html', {'form': form})
