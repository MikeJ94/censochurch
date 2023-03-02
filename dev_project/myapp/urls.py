from django import urls
from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

#from myapp.views import CountryAutocomplete

urlpatterns = [
    
    #------------Personas-------------------
    path('',views.home),  
    #path('listarPersonas/',login_required(views.listarPersonas)), 
    path('personas/list/', login_required(views.PersonaListView.as_view()), name='person_list'),  
    #path('registrarPersona/',login_required(views.registrarPersona)),  
    path('personas/add/', login_required(views.PersonaCreateView.as_view()), name='person_create'),
    #path('listarPersonas/edicionPersona/<str:id>', login_required(views.editPerson), name = 'edit-per'), #Se Pinta los Valores, Se guardan los Nuevos Posibles Cambios
    path('personas/edit/<int:pk>/', login_required(views.PersonaUpdateView.as_view()), name = 'person_edit'), #Se Pinta los Valores, Se guardan los Nuevos Posibles Cambios
    #path('listarPersonas/edicionPersona/<id>', views.edicionPersona"), Se Pinta los Valores Primero
    #path('editarPersona/', views.editarPersona), Luego se Guardan los Nuevos Valores
    path('personas/list/eliminarPersona/<id>', login_required(views.eliminarPersona)),
    path('personas/view/<id>', login_required(views.verPersona), name = 'view-per'),
    #------------Personas-------------------

    #------------Hijos-------------------
    path('sons/list/',login_required(views.listarSons)),
    path('sons/add/',login_required(views.registrarHijo)),
    path('sons/edit/<str:id>', login_required(views.editHijo), name = 'edit-son'), #Se Pinta los Valores, Se guardan los Nuevos Posibles Cambios
    #------------Hijos-------------------

    #------------Dashboards-------------------
    path('verdashboard/',login_required(views.verdashboard)),
    #------------Dashboards-------------------
    
    #------------Relacionales-------------------
    path('listarph/',login_required(views.listarph)),
    path('listarpm/',login_required(views.listarpm)),
    path('listarhm/',login_required(views.listarhm))
     #------------Relacionales-------------------

]
