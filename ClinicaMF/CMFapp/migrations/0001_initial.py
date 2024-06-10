# Generated by Django 5.0.6 on 2024-06-09 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profissional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('cpf', models.CharField(max_length=14, unique=True)),
                ('data_nascimento', models.DateField()),
                ('telefone', models.CharField(max_length=15)),
                ('genero', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')], max_length=1)),
                ('instituicao_de_formacao', models.CharField(max_length=255)),
                ('CMR', models.CharField(max_length=20)),
                ('area_de_atuacao', models.CharField(choices=[('PSICOLOGIA', 'Psicologia'), ('PSIQUIATRIA', 'Psiquiatria')], max_length=12)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
    ]
