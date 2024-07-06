from django.shortcuts import render, redirect
from .forms import VerazForm, NombreApellidoTelefonoCUILForm

def index(request):
    return render(request, 'veraz/index.html')

def veraz(request):
    if request.method == 'POST':
        form_veraz = VerazForm(request.POST)
        if form_veraz.is_valid():
            opcion_elegida = int(form_veraz.cleaned_data['opcion'])

            if opcion_elegida == 1:
                return redirect('deuda_5_anios')
            elif opcion_elegida == 2:
                return redirect('deuda_menos')
            elif opcion_elegida == 3:
                return redirect('tarjeta_3_anios')
            elif opcion_elegida == 4:
                return redirect('tarjeta_menos')

        return render(request, 'veraz/verificacion.html', {'form': form_veraz})

    else:
        form_veraz = VerazForm()

    return render(request, 'veraz/verificacion.html', {'form': form_veraz})

def deuda_5_anios(request):
    if request.method == 'POST':
        form_nombre_apellido_telefono_cuil = NombreApellidoTelefonoCUILForm(request.POST)
        if form_nombre_apellido_telefono_cuil.is_valid():
            # Guardar los datos si es necesario
            # Redirigir a la página de datos guardados
            return redirect('datos_guardados')

    # Si no se ha enviado el formulario o no es válido, mostrar el formulario
    form_nombre_apellido_telefono_cuil = NombreApellidoTelefonoCUILForm()
    return render(request, 'veraz/deuda_5_anios_form.html', {'form': form_nombre_apellido_telefono_cuil})
def deuda_menos(request):
    if request.method == 'POST':
        form_nombre_apellido_telefono_cuil = NombreApellidoTelefonoCUILForm(request.POST)
        if form_nombre_apellido_telefono_cuil.is_valid():
            # Procesar el formulario y redirigir a datos_guardados.html
            return redirect('datos_guardados')

    form_nombre_apellido_telefono_cuil = NombreApellidoTelefonoCUILForm()
    return render(request, 'veraz/deuda_menos_5_anios_form.html', {'form': form_nombre_apellido_telefono_cuil})

def tarjeta_3_anios(request):
    if request.method == 'POST':
        form_nombre_apellido_telefono_cuil = NombreApellidoTelefonoCUILForm(request.POST)
        if form_nombre_apellido_telefono_cuil.is_valid():
            # Procesar el formulario y redirigir a datos_guardados.html
            return redirect('datos_guardados')

    form_nombre_apellido_telefono_cuil = NombreApellidoTelefonoCUILForm()
    return render(request, 'veraz/deuda_5_anios_form.html', {'form': form_nombre_apellido_telefono_cuil})

def tarjeta_menos(request):
    if request.method == 'POST':
        form_nombre_apellido_telefono_cuil = NombreApellidoTelefonoCUILForm(request.POST)
        if form_nombre_apellido_telefono_cuil.is_valid():
            # Procesar el formulario y redirigir a datos_guardados.html
            return redirect('datos_guardados')

    form_nombre_apellido_telefono_cuil = NombreApellidoTelefonoCUILForm()
    return render(request, 'veraz/deuda_menos_5_anios_form.html', {'form': form_nombre_apellido_telefono_cuil})

def datos_guardados(request):
    return render(request, 'veraz/datos_guardados.html')
