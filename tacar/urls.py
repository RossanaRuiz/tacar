"""tacar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from core.views import home
from core.views import cadastro_cliente
from core.views import listagem_cliente
from core.views import cadastro_veiculo
from core.views import listagem_veiculo
from core.views import cadastro_fabricante
from core.views import listagem_fabricante
from django.conf.urls.static import static
from django.conf import settings
from core.views import home, cadastro_cliente, listagem_cliente, cadastro_veiculo, cadastro_fabricante, listagem_veiculo,\
    listagem_fabricante, Registrar, atualiza_cliente, atualiza_veiculo, atualiza_fabricante, exclui_cliente, exclui_veiculo, exclui_fabricante, \
    cadastro_tabelaPreco, listagem_tabelaPreco, atualiza_tabelaPreco, exclui_tabelaPreco, cadastro_rotativo, listagem_rotativo, cadastro_mensalista, \
    listagem_mensalista, atualiza_mensalista, exclui_mensalista,atualiza_rotativo, exclui_rotativo



urlpatterns = [
    path('admin/', admin.site.urls),
    path('captcha/', include('captcha.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/registrar/', Registrar.as_view(), name='url_principal'),
    path('', home, name='url_principal'),
    path('cadastro_cliente/', cadastro_cliente, name='url_cadastro_cliente'),
    path('cadastro_veiculo/',cadastro_veiculo, name='url_cadastro_veiculo'),
    path('cadastro_fabricante/', cadastro_fabricante, name='url_cadastro_fabricante'),
    path('cadastro_tabelaPreco/', cadastro_tabelaPreco, name='url_cadastro_tabelaPreco'),
    path('cadastro_rotativo/', cadastro_rotativo, name='url_cadastro_rotativo'),
    path('cadastro_mensalista/', cadastro_mensalista, name='url_cadastro_mensalista'),
    path('listagem_cliente/', listagem_cliente, name='url_listagem_cliente'),
    path('listagem_veiculo/',listagem_veiculo, name='url_listagem_veiculo'),
    path('listagem_fabricante/', listagem_fabricante, name='url_listagem_fabricante'),
    path('listagem_tabelaPreco/', listagem_tabelaPreco, name='url_listagem_tabelaPreco'),
    path('listagem_rotativo/', listagem_rotativo, name='url_listagem_rotativo'),
    path('listagem_mensalista/', listagem_mensalista, name='url_listagem_mensalista'),
    path('atualiza_cliente/<int:id>/', atualiza_cliente, name='url_atualiza_cliente'),
    path('atualiza_veiculo/<int:id>/', atualiza_veiculo, name='url_atualiza_veiculo'),
    path('atualiza_fabricante/<int:id>/', atualiza_fabricante, name='url_atualiza_fabricante'),
    path('atualiza_tabelaPreco/<int:id>/', atualiza_tabelaPreco, name='url_atualiza_tabelaPreco'),
    path('atualiza_mensalista/<int:id>/', atualiza_mensalista, name='url_atualiza_mensalista'),
    path('atualiza_rotativo/<int:id>/', atualiza_rotativo, name='url_atualiza_rotativo'),
    path('exclui_cliente/<int:id>/', exclui_cliente, name='url_exclui_cliente'),
    path('exclui_veiculo/<int:id>/', exclui_veiculo, name='url_exclui_veiculo'),
    path('exclui_fabricante/<int:id>/', exclui_fabricante, name='url_exclui_fabricante'),
    path('exclui_tabelaPreco/<int:id>/', exclui_tabelaPreco, name='url_exclui_tabelaPreco'),
    path('exclui_mensalista/<int:id>/', exclui_mensalista, name='url_exclui_mensalista'),
    path('exclui_rotativo/<int:id>/', exclui_rotativo, name='url_exclui_rotativo'),



]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
