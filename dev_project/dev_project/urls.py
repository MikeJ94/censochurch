"""dev_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from myapp.views import Inicio
from usuario.views import Login, logoutUsuario
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include(('myapp.urls','myapp'))),
    path('', login_required(Inicio.as_view()), name='inicio'),
    path('accounts/login/', Login.as_view(), name = 'login'),
    path('logout/',login_required(logoutUsuario), name ='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



