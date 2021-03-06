"""api_django_microservices URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_nested import routers

from clientes.api.viewsets import ClienteViewSet, ContatoViewSet

router = routers.DefaultRouter()

router.register("clientes", ClienteViewSet, basename="clientes")
router.register("contatos", ContatoViewSet, basename="contatos")

clientes_router = routers.NestedSimpleRouter(router, "clientes", lookup="cliente")
clientes_router.register("contatos", ContatoViewSet, basename="contato")


urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("api/v1/", include(clientes_router.urls)),
    path("admin/", admin.site.urls),
]

# Configuração de rotas do serviço
from clientes.handlers import grpc_handlers as cliente_grpc_handlers

# LISTA DE SERVIÇOS CRIADOS
def grpc_handlers(server):
    cliente_grpc_handlers(server)
