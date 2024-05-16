# Generated by Django 5.0.1 on 2024-02-05 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.IntegerField(max_length=10)),
                ('mensaje', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Experiencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cargo', models.CharField(max_length=50)),
                ('institucion', models.CharField(max_length=50)),
                ('fechaDeInicio', models.DateField()),
                ('fechaDeEgreso', models.DateField()),
                ('descripcion', models.CharField(max_length=100)),
                ('contacto', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Portafolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('lenguaje', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
    ]