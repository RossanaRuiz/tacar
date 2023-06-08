from django.db import models
from math import ceil, floor

# Create your models here.
from unicodedata import decimal


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100,blank=True, null=True, verbose_name='Endereço')
    complemento = models.CharField(max_length= 100, blank=True, null=True, verbose_name='Complemento')
    bairro = models.CharField(max_length= 100, blank=True, null=True, verbose_name='Bairro')
    cidade = models.CharField(max_length=100, blank=True, null=True, verbose_name='Cidade')
    email = models.EmailField(verbose_name='E-mail')
    fone = models.CharField(max_length=20, blank=True, null=True, verbose_name='Telefone')
    foto = models.ImageField(upload_to='foto_cliente',blank=True, null=True, verbose_name='Foto')
    class Meta:
        verbose_name_plural='Clientes'
    def __str__(self):
        return self.nome

class Fabricante(models.Model):
    nome = models.CharField(max_length=50, verbose_name='Fabricante')
    url = models.URLField(verbose_name='Site', blank=True, null=True)
    logo = models.ImageField(upload_to='logo_fabricante',blank=True, null=True, verbose_name='Logo')
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name_plural='Fabricantes'

class Veiculo(models.Model):
    placa = models.CharField(max_length=10, verbose_name='Placa')
    modelo = models.CharField(max_length=30, blank=True, null=True, verbose_name='Modelo')
    fabricante_id = models.ForeignKey(Fabricante, on_delete= models.CASCADE, verbose_name='Fabricante')
    cliente_id = models.ForeignKey(Cliente, on_delete= models.CASCADE, verbose_name='Cliente')
    cor = models.CharField(max_length=30, blank=True, null=True, verbose_name='Cor')
    ano = models.IntegerField(default=2023, blank=True, null=True, verbose_name='Ano')
    foto = models.ImageField(upload_to='foto_carro', blank=True, null=True, verbose_name='')

    class Meta:
        verbose_name_plural='Veículos'
    def __str__(self):
        return f"{self.placa}  ({self.modelo})"

class TabelaPreco(models.Model):
    descricao = models.CharField(max_length=100,verbose_name='Descricao')
    valor = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Valor')

    class Meta:
        verbose_name_plural = 'TabelaPreços'

    def __str__(self):
        return f"{self.descricao} = {self.valor}"


class Mensalista(models.Model):
    id_veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE, verbose_name='Veiculo')
    id_tabela = models.ForeignKey(TabelaPreco, on_delete=models.CASCADE, verbose_name='Preco')
    observacoes = models.TextField(blank=True, null=True, verbose_name='Obs. ')
    class Meta:
        verbose_name_plural = "Mensalistas"
    def __str__(self):
        return f'{self.id_veiculo}:{self.id_tabela}'


class Rotativo(models.Model):
    data_hora_entrada = models.DateTimeField(auto_now=False, verbose_name='Entrada')
    data_hora_saida = models.DateTimeField(auto_now=False, blank=True, null=True, verbose_name='Saida')
    id_veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE, verbose_name='Veiculo')
    id_tabela = models.ForeignKey(TabelaPreco, on_delete=models.CASCADE, verbose_name='Preço')
    total = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True, verbose_name='Total' )
    pago = models.BooleanField(default=False, blank=False, verbose_name='Pago')
    observacoes = models.TextField(blank=True, null=True, verbose_name='Obs. ')


    class Meta:
        verbose_name_plural = 'Rotativos'
    def __str__(self):
        return f'{self.data_hora_entrada}:{self.id_veiculo.placa}'

    def calcula_total(self):
        if self.data_hora_saida:
            hora = (self.data_hora_saida - self.data_hora_entrada).total_seconds()/3600
            obj = TabelaPreco.objects.get(id=self.id_tabela.pk)
            if hora <= 0.5:
                self.total = obj.valor/2
            else:
                self.total = ceil(hora) * obj.valor
            return self.total
        else:
            return 0.0