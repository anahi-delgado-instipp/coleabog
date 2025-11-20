# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from . import views


urlpatterns = [

 #Pagina Informativa
   path('', views.pagina_informatica, name='pagina_informatica'),
   path('start/', views.start_page, name='start_page')

   
]
