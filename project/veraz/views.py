from django.shortcuts import render, redirect
from .forms import VerazForm, NombreApellidoTelefonoCUILForm, HistorialForm
from .models import Formulario, Datos, RegistroHistorial

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
            # Guardar los datos en la base de datos
            form_data = form_nombre_apellido_telefono_cuil.cleaned_data
            Datos.objects.create(
                nombre=form_data['nombre'],
                apellido=form_data['apellido'],
                cuil=form_data['cuil'],
                telefono=form_data['telefono']
            )
            return redirect('datos_guardados')

    form_nombre_apellido_telefono_cuil = NombreApellidoTelefonoCUILForm()
    return render(request, 'veraz/deuda_5_anios_form.html', {'form': form_nombre_apellido_telefono_cuil})

def deuda_menos(request):
    if request.method == 'POST':
        form_nombre_apellido_telefono_cuil = NombreApellidoTelefonoCUILForm(request.POST)
        if form_nombre_apellido_telefono_cuil.is_valid():
            form_data = form_nombre_apellido_telefono_cuil.cleaned_data
            Formulario.objects.create(
                nombre=form_data['nombre'],
                apellido=form_data['apellido'],
                numero_gestion=form_data.get('numero_gestion', '')
            )
            return redirect('datos_guardados')

    form_nombre_apellido_telefono_cuil = NombreApellidoTelefonoCUILForm()
    return render(request, 'veraz/deuda_menos_5_anios_form.html', {'form': form_nombre_apellido_telefono_cuil})

def tarjeta_3_anios(request):
    if request.method == 'POST':
        form_nombre_apellido_telefono_cuil = NombreApellidoTelefonoCUILForm(request.POST)
        if form_nombre_apellido_telefono_cuil.is_valid():
            form_data = form_nombre_apellido_telefono_cuil.cleaned_data
            Datos.objects.create(
                nombre=form_data['nombre'],
                apellido=form_data['apellido'],
                cuil=form_data['cuil'],
                telefono=form_data['telefono']
            )
            return redirect('datos_guardados')

    form_nombre_apellido_telefono_cuil = NombreApellidoTelefonoCUILForm()
    return render(request, 'veraz/deuda_5_anios_form.html', {'form': form_nombre_apellido_telefono_cuil})

def tarjeta_menos(request):
    if request.method == 'POST':
        form_nombre_apellido_telefono_cuil = NombreApellidoTelefonoCUILForm(request.POST)
        if form_nombre_apellido_telefono_cuil.is_valid():
            form_data = form_nombre_apellido_telefono_cuil.cleaned_data
            Formulario.objects.create(
                nombre=form_data['nombre'],
                apellido=form_data['apellido'],
                numero_gestion=form_data.get('numero_gestion', '')
            )
            return redirect('datos_guardados')

    form_nombre_apellido_telefono_cuil = NombreApellidoTelefonoCUILForm()
    return render(request, 'veraz/deuda_menos_5_anios_form.html', {'form': form_nombre_apellido_telefono_cuil})

def datos_guardados(request):
    return render(request, 'veraz/datos_guardados.html')

def historial_view(request):
    if request.method == 'POST':
        form = HistorialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('datos_guardados')  # O la URL a la que deseas redirigir después de guardar
        else:
            print(form.errors)  # Para depuración: imprime los errores del formulario
    else:
        form = HistorialForm()
    
    return render(request, 'veraz/historial.html', {'form': form})

def quienes_somos(request):
    return render(request, 'veraz/quienes_somos.html')