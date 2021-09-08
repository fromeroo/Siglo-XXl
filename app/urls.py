from django.urls import path
from .views import intranet, login

urlpatterns = [
    path('intranet/', intranet, name="intranet"),
    path('login/', login, name="login"),
]
