from django.contrib import admin
from .models import Contacto, Marca, Producto, Accesorios

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio", "peso", "marca"]
    list_editable = ["precio"]
    search_fields = ["nombre"]
    list_filter = ["marca","peso"]
    list_per_page = 5


admin.site.register(Marca)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Contacto)
admin.site.register(Accesorios)