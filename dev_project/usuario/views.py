from http.client import HTTPResponse
from urllib import request
from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse_lazy #Accediendo a una Forma de redireccionamiento
from django.utils.decorators import method_decorator #Accediendo a la Funcionalidad que nos permitira generar y capturar los errores,
from django.views.decorators.cache import never_cache #Medida de Seguridad para que no se guarden datos en Cache.
from django.views.decorators.csrf import csrf_protect #Medida de Seguridad 
from django.views.generic.edit import FormView #Accediendo a Vista Basada en Clase usada para trabajar con Formularios directamente.
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from .forms import FormularioLogin #Accediendo al Formualario

class Login(FormView):
    template_name = 'login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('inicio')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated: #Verifica Si es que existe un Usuario loggeado en la peticion
            return HttpResponseRedirect(self.get_success_url()) #Mandalo a BaseSlider
        else: #Sino
            return super(Login,self).dispatch(request,*args,**kwargs) #Mandalo al Login

    def form_valid(self, form):
        login(self.request,form.get_user())
        return super(Login, self).form_valid(form)

def logoutUsuario(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')
