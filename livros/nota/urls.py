from django.urls import path
from nota import views


urlpatterns = [
    path('', views.etiqueta_list, name='nota'),
]

