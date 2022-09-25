import imp
from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Marca, Accesorios
from .forms import ContactoForm, ProductoForm, CustomUserCreationForm, AccesoriosForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework import viewsets
from .serializers import ProductoSerializer, MarcaSerializer, AccesoriosSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, renderers, viewsets
from rest_framework.reverse import reverse



#Vistas

# api marca
class marca_list(generics.ListCreateAPIView):
    #Lista todo el codigo de producto, o crea uno nuevo.
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

# api Producto

class product_list(generics.ListCreateAPIView):
    #Lista todo el codigo de producto, o crea uno nuevo.
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
        

class product_detail(generics.RetrieveUpdateDestroyAPIView):
    #Trae, actualiza o borra el codigo completo de producto.
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# api accesorio

class accesorio_list(generics.ListCreateAPIView):
    #Lista todo el codigo de producto, o crea uno nuevo.
    queryset = Accesorios.objects.all()
    serializer_class = AccesoriosSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class accesorio_detail(generics.RetrieveUpdateDestroyAPIView):
    #Trae, actualiza o borra el codigo completo de producto.
    queryset = Accesorios.objects.all()
    serializer_class = AccesoriosSerializer
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class MarcaViewSet(viewsets.ModelViewSet):

    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class AccesorioViewSet(viewsets.ModelViewSet):
    
    queryset = Accesorios.objects.all()
    serializer_class = AccesoriosSerializer



def home(request):
    return render(request, 'app/home.html')

def quienesSomos(request):
    return render(request, 'app/quienesSomos.html')

def nuestrosMininos(request):
    return render(request, 'app/nuestrosMininos.html')

def formulario(request):
    data = {
        'form': ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "mensaje guardado"
        else:
            data["form"] = formulario


    return render(request, 'app/formulario.html', data)

def productos(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'app/productos.html', data)

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(usarname=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            messages.success(request, "Registrado correctamente")
            return redirect(to="home")
        data["form"] = formulario
    return render(request, 'registration/registro.html', data)

def pokedex(request):
    return render(request, 'app/pokedex.html')  

@permission_required('app.add_producto')
def agregar_producto(request):
    data={
        'form': ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto registrado")
        else:
            data["form"] = formulario

    return render(request, 'app/producto/agregar.html', data)

@permission_required('app.view_producto')
def listar_productos(request):
    productos = Producto.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(productos, 5)
        productos = paginator.page(page)
    except:
        raise Http404

    data = {
        'entity': productos,
        'paginator': paginator
    }
    return render(request, 'app/producto/listar.html',data)

@permission_required('app.change_producto')
def modificar_producto(request, id):

    producto = get_object_or_404(Producto, id=id)

    data = {
        'form': ProductoForm(instance=producto)

    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado correctamente")
            return redirect(to="listar_productos")
        data["form"] = formulario


    return render(request, 'app/producto/modificar.html', data)

@permission_required('app.delete_producto')
def eliminar_producto(request, id):

    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect(to="listar_productos")


def accesorios (request):
    accesorios = Accesorios.objects.all()
    data = {
        'accesorios': accesorios
    }
    return render(request, 'app/Accesorios.html', data)

@permission_required('app.add_Accesorios')
def agregarAcc(request):
    data={
        'form': AccesoriosForm()
    }
    if request.method == 'POST':
        formulario = AccesoriosForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Accesorio Registrado")
        else:
            data["form"] = formulario

    return render(request, 'app/Accesorios/agregarAcc.html', data)

@permission_required('app.view_Accesorios')
def listar_Accesorios(request):
    accesorios = Accesorios.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(accesorios, 5)
        accesorios = paginator.page(page)
    except:
        raise Http404

    data = {
        'entity': accesorios,
        'paginator': paginator
    }
    return render(request, 'app/Accesorios/listarAcc.html',data)

@permission_required('app.change_Accesorios')
def modificar_Accesorios(request, id):

    accesorios = get_object_or_404(Accesorios, id=id)

    data = {
        'form': AccesoriosForm(instance=accesorios)

    }

    if request.method == 'POST':
        formulario = AccesoriosForm(data=request.POST, instance=accesorios, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado correctamente")
            return redirect(to="listar_accesorios")
        data["form"] = formulario


    return render(request, 'app/Accesorios/modificarACC.html', data)

@permission_required('app.delete_accesorios')
def eliminar_Accesorios(request, id):

    accesorios = get_object_or_404(Accesorios, id=id)
    accesorios.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect(to="listar_accesorios")
