from CMFapp.models import *

class Atendente(models.Model):
    # criado_em = models.DateTimeField(auto_now_add=True) ----> O criado_em armazena a data em que o objeto da classe foi adicionado.
    # alterado_em = models.DateTimeField(auto_now=True) ----> O alterado_em armazena a data da última modificação do objeto.
    GENERO_CHOICES = (('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro'),)

    nome = models.CharField(max_length=150)
    CPF = models.CharField(max_length=14, unique=True)  # Assumindo que o CPF é uma string formatada, como "123.456.789-10"
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=15)
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES)
    # area_de_atuacao = models.CharField(max_length=12, choices=ESPECIALIDADE_CHOICES)
    email = models.EmailField(unique=True)
    foto_de_perfil = models.ImageField(null=True, blank=True)
    # username
    # password

    def __str__(self):
        return '{}'.format(self. nome)