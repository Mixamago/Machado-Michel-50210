from django.http import HttpResponse
from django.template import loader

def prueba(request):
        return HttpResponse('Estoy probando mi view.')

def home(request):
        return HttpResponse('Página de inicio.')

def signup(request):
        return HttpResponse('Página de registro.')

def signup_done(request):
        return HttpResponse('Página de registro exitoso.')

def login(request):
        return HttpResponse('Página de inicio de sesión.')

def about(request):
        return HttpResponse('Página acerca de mí.')