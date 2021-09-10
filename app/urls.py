from django.urls import path
from .views import intranet, index, register

urlpatterns = [
    path('intranet/', intranet, name="intranet"),
    path('register/', register, name="register"),
    path('', index, name="index"),
]
