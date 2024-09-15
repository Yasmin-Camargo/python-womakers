from django.contrib import admin
from django.urls import path

from base.views import inicio, cadastro

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio),
    path('cadastro/', cadastro)
]
