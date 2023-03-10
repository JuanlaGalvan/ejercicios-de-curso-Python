"""primer_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path

from primer_django.views import hola_Mundo, otra_mas, fecha_actual, vista_con_edad, vista_con_templete, saludo_desde_templete
#asi le indico mas especificamente de donde las views

#ya vienen instaladas url pero yo creo las mias e inporto de donde
urlpatterns =[
    path('admin/', admin.site.urls),
    path('hola/', hola_Mundo, name='hola_mundo'), 
    path('otra/', otra_mas),
    path('fecha/', fecha_actual),
    path('edad/<int:edad>/', vista_con_edad),
    path('vista-con-templete/', vista_con_templete),
    path('saludo_desde_templete/', saludo_desde_templete),

]
