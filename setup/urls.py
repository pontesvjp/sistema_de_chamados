
from django.contrib import admin
from django.urls import path
from chamados.views import index, novo_chamado

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('novo_chamado/', novo_chamado, name="novo_chamado"),
]
