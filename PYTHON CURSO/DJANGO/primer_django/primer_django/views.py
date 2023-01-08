from django.http import HttpResponse 
from django.shortcuts import render #Asi importo los http de django
from datetime import datetime

def hola_Mundo(request):
    return HttpResponse("Hola Mundo") #siempre tengo que inportar los http

def otra_mas(request):
    return HttpResponse('Si, otra mas...')
    
def fecha_actual(request):
    hoy = datetime.now().date() #asi solo me responde solo fecha
    return HttpResponse(f'la fecha de hoy es {hoy}') 

def vista_con_edad(request, edad):
    return HttpResponse(f'Esto funciona? la edad es {edad}?')
    
def vista_con_templete(request):
    return render (request, 'templete.html', context={})

def saludo_desde_templete(request):
        context= {
        'nombre': 'Juan',
        'edad': '48',
        'nacionalidad':'argentina',
        'trabaja': True,
        'tareas': ['alarmas', 'cctv', 'redes', 'control de accesos'],
        


    }
        return render(request, 'saludo.html', context=context)    