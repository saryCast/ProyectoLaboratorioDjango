from django.shortcuts import render,redirect
from .models import Laboratorio
# Create your views here.
def index(request):
    return render(request,'index.html')

def mostrar_lab(request):
    laboratorios = Laboratorio.objects.all()
    return render(request,'mostrar.html',{'laboratorios':laboratorios} )

def insertar_lab(request):
    if request.method =="POST":
        nombre = request.POST['nombre']
        ciudad = request.POST['ciudad']
        pais = request.POST['pais']
        laboratorio = Laboratorio(nombre=nombre, ciudad=ciudad, pais=pais)
        laboratorio.save()
        return redirect('mostrar-lab')
    else:
        return render(request,'insertar.html')

def editar_lab(request,id):
 laboratorio = Laboratorio.objects.get(id=id)
 return render(request,'editar.html',{'laboratorio':laboratorio})

def eliminar_lab(request,id):
  laboratorio=Laboratorio.objects.get(id=id)

  if request.method=='POST':
    laboratorio.delete()
    return redirect('/laboratorio/mostrar')
  return render(request,'eliminar.html',{'laboratorio':laboratorio})

def actualizar_lab(request,id):
   if request.method == "POST":
    nombre=request.POST['lab_nombre']
    ciudad=request.POST['lab_ciudad']
    pais=request.POST['lab_pais']
    laboratorio = Laboratorio.objects.get(id=id)
    laboratorio.nombre =nombre
    laboratorio.ciudad =ciudad
    laboratorio.pais =pais
    laboratorio.save()
    return redirect('mostrar-lab')
   else:
        # Manejo del caso GET (opcional, si necesitas mostrar un formulario)
        laboratorio = Laboratorio.objects.get(id=id)
        return render(request, 'editar.html', {'laboratorio': laboratorio})