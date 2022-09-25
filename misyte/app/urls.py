from django.urls import path, include
from .views import accesorios, agregarAcc, eliminar_Accesorios, home, listar_Accesorios, modificar_Accesorios, nuestrosMininos, quienesSomos, formulario, productos, agregar_producto, listar_productos, \
modificar_producto, eliminar_producto, registro, product_list, product_detail, APIView, marca_list, accesorio_list, accesorio_detail, \
MarcaViewSet, ProductoViewSet, AccesorioViewSet, pokedex
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns


#localhost:8000/api/producto/
urlpatterns = [
    path('', home, name="home"),
    path('quienesSomos/', quienesSomos, name="quienesSomos"),
    path('nuestrosMininos/', nuestrosMininos, name="nuestrosMininos"),
    path('formulario/', formulario, name="formulario"),
    path('productos/', productos, name="productos"),
    path('agregar-productos/', agregar_producto, name="agregar_producto"),
    path('listar-productos/', listar_productos, name="listar_productos"),
    path('modificar-producto/<id>/', modificar_producto, name="modificar_producto"),
    path('eliminar-producto/<id>/', eliminar_producto, name="eliminar_producto"),
    path('registro/', registro, name="registro"),
    path('pokedex/', pokedex, name="pokedex"),
    path('Accesorios/', accesorios, name="Accesorios"),
    path('agregarAcc/', agregarAcc, name="agregar_accesorios"),
    path('listarAcc/', listar_Accesorios, name="listar_accesorios"),
    path('eliminarAcc/<id>/', eliminar_Accesorios, name="eliminar_accesorios"),
    path('modificarAcc/<id>/', modificar_Accesorios, name="modificar_accesorios"),
    path('marcaApi/', marca_list.as_view()),
    path('productoApi/', product_list.as_view()),
    path('productoApi/<int:pk>/', product_detail.as_view()),
    path('accesorioApi/', accesorio_list.as_view()),
    path('accesorioApi/<int:pk>/', accesorio_detail.as_view()),
    ]
