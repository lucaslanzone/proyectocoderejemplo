from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, "appcoder/index.html")

def estudiantes(request):
    return HttpResponse("vista de estudiantes")

def profesores(request):
    return HttpResponse("vista de profesores")

def cursos(request):
    return HttpResponse("vista de cursos")

def entregables(request):
    return HttpResponse("vista de entregables")
