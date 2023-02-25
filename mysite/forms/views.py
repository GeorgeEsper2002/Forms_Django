from django.shortcuts import render, redirect
from .models import Usuarios
from .forms import RegistrarUsuario
def index(request):
    mis_usuarios = Usuarios.objects.all()
    if request.method == 'POST':
        register_form = RegistrarUsuario(request.POST)
        if register_form.is_valid():
            success = register_form.registrar_usuario()
            return redirect('./')
    else:
        register_form = RegistrarUsuario()
        return render(request, 'forms/mi_form.html', {'register_form': register_form,'usuarios': mis_usuarios})







'''from django.shortcuts import render
# Create your views here.
from .forms import RegistrarUsuario
def index(request):
    if request.method =='POST':
        register_form=RegistrarUsuario(request.Post)
        if register_form.is_valid():
            success=register_form.registrar_usuario(request.user)
            return redirect('./')
    else:
        #Aqui muestra nuestro form
        register_form=RegistrarUsuario()
        return render(request,'forms/mi_forms.html',{'register_form':register_form}) '''