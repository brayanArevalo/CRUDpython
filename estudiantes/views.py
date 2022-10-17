from django.shortcuts import render,redirect
from .models import asignatura, asignaturaxgrupo, estudiante,grupo, profesor



#VISTAS DEL MENÚ
def index(request):
    return render(request,"index.html")

def contactanos(request):
    return render(request,"contactanos.html")

def nosotros(request):
    return render(request,"nosotros.html")

def demofree(request):
    return render(request,"demofree.html")

# def salir(request):
#     return render(request,"index.html")
#FIN DE LAS VISTAS DEL MENÚ

#CRUD ESTUDIANTES
#CREAR
def registrarEstudiante(request):
    nombre = request.POST['nombre']
    apellido = request.POST['apellido']
    grupo = request.POST['grupo']
    estudiantee = estudiante.objects.create(nombre=nombre, apellido=apellido,grupo_id=grupo)
    return redirect('/demofree/estudiantes/')
    
#LISTAR 
def estudiantes(request):
    estudianteLista = estudiante.objects.all()
    grupoLista = grupo.objects.all()
    print(estudianteLista)
    print(grupoLista)
    return render(request,"estudiantes.html",{"estudiantes": estudianteLista,"grupos":grupoLista})

#ELIMINAR
def eliminarEstudiante(request , id):
    estudiantee = estudiante.objects.get(id=id)
    estudiantee.delete()
    return redirect('/demofree/estudiantes/')

#ACTUALIZAR
def editarEstudiante(request,id):
    estudianteLista = estudiante.objects.get(id=id)
    grupoLista = grupo.objects.all()
    return render(request,"editarEstudiante.html",{"estudiantes": estudianteLista,"grupos":grupoLista})  
    print(editarEstudiante)

def modificarEstudiante(request):
    nombre = request.POST['nombre']
    apellido = request.POST['apellido']
    grupo = request.POST['grupo']
    id = request.POST['id']
    
    estudiantee = estudiante.objects.get(id=id)
    estudiantee.pk=id
    estudiantee.nombre = nombre
    estudiantee.apellido=apellido
    estudiantee.grupo_id = grupo
    estudiantee.save()
    return redirect('/demofree/estudiantes/')
#FIN RUD ESTUDIANTES

#CRUD PROFESORES
#LISTAR
def profesores(request):
    profesorLista = profesor.objects.all()
    return render(request,"profesores.html",{"profesores": profesorLista})

#CREAR
def registrarProfesor(request):
    nombre = request.POST['nombre']
    apellido = request.POST['apellido']
    telefono = request.POST['telefono']
    profesorr = profesor.objects.create(nombre=nombre,apellido=apellido,telefono=telefono)
    return redirect('/demofree/profesores/')

#ELIMINAR
def eliminarProfesor(request , id):
    profesorr = profesor.objects.get(id=id)
    profesorr.delete()
    return redirect('/demofree/profesores/')
#EDITAR
def editarProfesor(request,id):
    profesorLista = profesor.objects.get(id=id)
    return render(request,"editarProfesor.html",{"profesores": profesorLista}) 

def modificarProfesor(request):
    nombre = request.POST['nombre']
    apellido = request.POST['apellido']
    telefono = request.POST['telefono']
    profe_id = request.POST['id']
    
    profesorr = profesor.objects.get(id=profe_id)
    profesorr.pk=profe_id
    profesorr.nombre = nombre
    profesorr.apellido=apellido
    profesorr.telefono=telefono
    profesorr.save()
    return redirect('/demofree/profesores/')   

#ASIGNATURAS
def asignaturas(request):
    profesorLista = profesor.objects.all()
    asignaturaLista = asignatura.objects.all()
    return render(request,"asignaturas.html",{"asignaturas": asignaturaLista,"profesores":profesorLista})

def registrarAsignatura(request):
    nombre = request.POST['nombre']
    profesor = request.POST['profesor']
    asignaturaa = asignatura.objects.create(nombre = nombre,profesor_id=profesor)
    return redirect('/demofree/asignaturas/')

def eliminarAsignatura(request,id):
    asignaturaa = asignatura.objects.get(id=id)
    asignaturaa.delete()
    return redirect('/demofree/asignaturas/')

def editarAsignatura(request,id):
    profesorLista = profesor.objects.all()
    asignaturaLista = asignatura.objects.get(id=id)
    return render(request,"editarAsignatura.html",{"asignaturas": asignaturaLista,"profesores":profesorLista}) 

def modificarAsignatura(request):
    id = request.POST['id']
    nombre = request.POST['nombre']
    profesor = request.POST['profesor']
    asignaturaLista = asignatura.objects.get(id=id)
    asignaturaLista.pk=id
    asignaturaLista.nombre=nombre
    asignaturaLista.profesor_id= profesor
    asignaturaLista.save()
    return redirect('/demofree/asignaturas/')

#GRUPOS
def grupos(request):
    grupoLista = grupo.objects.all()
    return render(request,"grupos.html",{"grupos":grupoLista})

def registrarGrupo(request):
    nombre = request.POST['nombre']
    cantidad = request.POST['cantidad']

    grupoo = grupo.objects.create(nombre=nombre,cant_estudiantes=cantidad)
    return redirect('/demofree/grupos/')

def eliminarGrupo(request,id):
    grupoo = grupo.objects.get(id=id)
    grupoo.delete()
    return redirect('/demofree/grupos/')

def editarGrupo(request,id):
    grupoo = grupo.objects.get(id=id)
    return render(request,"editarGrupo.html",{"grupos":grupoo})

def modificarGrupo(request):
    id = request.POST['id']
    nombre = request.POST['nombre']
    cantidad = request.POST['cantidad']
    grupoo = grupo.objects.get(id=id)
    grupoo.pk = id
    grupoo.nombre = nombre
    grupoo.cant_estudiantes=cantidad
    return redirect('/demofree/grupos/')

def notas(request):
    estudianteLista = estudiante.objects.all()
    grupoLista = grupo.objects.all()
    notaLista = asignaturaxgrupo.objects.all()
    print(estudianteLista)
    print(notaLista)
    return render(request,"notas.html",{"estudiantes": estudianteLista,"grupos":grupoLista,"notas":notaLista})
