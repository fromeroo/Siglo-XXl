from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Proveedor, Menu, Caja, Mesa, Producto, Receta

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

class CustomProductoCreationForm(ModelForm):
    class Meta:
        model = Producto
        fields = "__all__"

class CustomRecetaCreationForm(ModelForm):
    class Meta:
        model = Receta
        fields = "__all__"