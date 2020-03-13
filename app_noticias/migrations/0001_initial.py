# Generated by Django 3.0.3 on 2020-03-06 23:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=64)),
                ('slug', models.SlugField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128, verbose_name='Nome')),
                ('data_nascimento', models.DateField(blank=True, null=True, verbose_name='Data de Nascimento')),
                ('telefone_celular', models.CharField(blank=True, help_text='Número de telefone celular formato (99) 99999-9999', max_length=15, null=True, verbose_name='Telefone celular')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='E-mail')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=128, null=True, verbose_name='título')),
                ('conteudo', models.TextField()),
                ('data_publicacao', models.DateField(blank=True, null=True, verbose_name='Data')),
                ('autor', models.ForeignKey(blank=True, max_length=128, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_noticias.Pessoa', verbose_name='Autor')),
                ('tags', models.ManyToManyField(to='app_noticias.Tag')),
            ],
            options={
                'verbose_name': 'Notícia',
                'verbose_name_plural': 'Notícias',
            },
        ),
    ]
