from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Proveedor, Menu, Caja

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