from django.contrib import admin
from core.models import Cliente, Fabricante, Veiculo, Mensalista, Rotativo, TabelaPreco



# Register your models here.
admin.site.register(Cliente)
admin.site.register(Fabricante)
admin.site.register(Veiculo)
admin.site.register(Mensalista)
admin.site.register(Rotativo)
admin.site.register(TabelaPreco)