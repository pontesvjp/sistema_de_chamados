from django.urls import path, include
from django.contrib import admin

urrlspatterns = [
    path('admin', admin.site.urls),
    path('', include('chamados.urls'))
     
]