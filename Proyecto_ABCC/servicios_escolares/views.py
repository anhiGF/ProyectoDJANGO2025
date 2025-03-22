from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView

from .models import Alumno
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django import forms

#altas 
class CrearAlumno(SuccessMessageMixin, CreateView):
    model = Alumno
    fields = "__all__"
    success_message = "Alumno agregado correctamente"

    def get_success_url(self):
        return reverse('Listar')

#bajas
class EliminarAlumno(SuccessMessageMixin, DeleteView):
    model = Alumno

    def get_success_url(self):
        messages.success(self.request, "Alumno eliminado correctamente")
        return reverse('Listar')

#cambios
class ActualizarAlumno(SuccessMessageMixin, UpdateView):
    model = Alumno
    form = Alumno 
    fields = "__all__"
    success_message = "Alumno modificado correcrtamente"

    def get_success_url(self):
        return reverse('Listar')
    
#consultar un alumno
class DetalleAlumno(DetailView):
    model = Alumno

#consultar todos los alumnos 
class ListarAlumnos(ListView):
    model = Alumno


def login_view(request):
    return render(request, 'login.html')
