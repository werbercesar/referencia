from django.urls import path
from catalogo import views


urlpatterns = [
    path('', views.index, name='index'),
    path('fontes/', views.ListaFontes.as_view(), name='fontes'),
    path('papeis/', views.CreatePapel.as_view(), name='papeis'),
    # path('papel/<int:pk>', views.LivroDetalheView.as_view(), name='detalhe_livro'),
]
