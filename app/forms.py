from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Proveedor, Menu, Caja, Mesa, Insumo, Receta, InventarioInsumo, Factura

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class CustomProveedorCreationForm(ModelForm):
    class Meta:
        model = Proveedor
        fields = "__all__"
class CustomMenusCreationForm(ModelForm):
    class Meta:
        model = Menu
        fields = "__all__"
class CustomCajasCreationForm(ModelForm):
    class Meta:
        model = Caja
        fields = "__all__"
class CustomMesasCreationForm(ModelForm):
    class Meta:
        model = Mesa
        fields = "__all__"

class CustomInsumoCreationForm(ModelForm):
    class Meta:
        model = Insumo
        fields = "__all__"

class CustomRecetaCreationForm(ModelForm):
    class Meta:
        model = Receta
        fields = "__all__"

class CustomInventarioInsumoCreationForm(ModelForm):
    class Meta:
        model = InventarioInsumo
        fields = "__all__"
class CustomFacturaCreationForm(ModelForm):
    class Meta:
        model = Factura
        fields = "__all__"