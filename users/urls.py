"""Definiuje wzorce aresów URL dla aplikacji"""

from django.urls import path, include

from . import views

app_name="users"
urlpatterns=[
    #Dołączanie domyślnych adresów uwierzytelniania
    path('',include('django.contrib.auth.urls')),

    #Strona rejestracji
    path('register/', views.register, name="register"),
]