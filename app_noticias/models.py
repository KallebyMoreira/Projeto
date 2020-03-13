from django.contrib.auth.models import User
from django.db import models



class Pessoa(models.Model):
    usuario = models.OneToOneField(User,on_delete = models.CASCADE,
        verbose_name = 'Usuário')
    nome = models.CharField("Nome", max_length=128)
    data_nascimento = models.DateField('Data de Nascimento',blank = True, null = True)
    telefone_celular = models.CharField("Telefone celular",max_length=15,
        help_text='Número de telefone celular formato (99) 99999-9999',
        blank=True, null= True)
    email = models.EmailField('E-mail',null=True,blank=True)

    def __str__(self):
        return self.nome

class Tag(models.Model):
    nome =  models.CharField(max_length=64)
    slug = models.SlugField(verbose_name="Previa da tag",max_length=64)

    def __str__(self):
        return self.nome

class Comentario(models.Model):
    pessoa = models.ForeignKey(Pessoa,on_delete= models.CASCADE,verbose_name="Autor")
    data_hora = models.DateTimeField(auto_now=True, verbose_name = "Data e Hora")
    comentario = models.CharField("Comentario",max_length=500)

class Categoria(models.Model):
    titulo  = models.CharField("Titulo",max_length=564, blank=True, null=True)
class Foto(models.Model):
    titulo  = models.CharField("Titulo",max_length=564, blank=True, null=True)
    url  = models.CharField("URL",max_length=564, blank=True, null=True)

class Noticia(models.Model):
    class Meta:
        verbose_name = 'Notícia'
        verbose_name_plural = 'Notícias'
    titulo = models.CharField('título',max_length=128, blank=True, null=True)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE, blank = True, null = True)
    conteudo = models.TextField()
    autor = models.ForeignKey(Pessoa,on_delete=models.CASCADE,verbose_name='Autor',max_length=128, blank=True, null=True)
    data_publicacao = models.DateField('Data', blank=True, null=True)
    tags = models.ManyToManyField(Tag)
    comentarios = models.ForeignKey(Comentario,on_delete=models.CASCADE,verbose_name = "Comentarios", blank = True,null = True)
    
    def __str__(self):
        return self.titulo


