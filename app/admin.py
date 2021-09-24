from django.contrib import admin
from .models import Banco, Boleta, Caja, CategoriaInsumo, Usuario
# Register your models here.

admin.site.register(Banco)
admin.site.register(Boleta)
admin.site.register(Caja)
admin.site.register(CategoriaInsumo)
admin.site.register(Usuario)