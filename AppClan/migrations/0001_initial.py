# Generated by Django 3.2.9 on 2021-12-14 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreComentarista', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('texto', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Integrante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=20)),
                ('fechaDeNacimiento', models.DateField()),
                ('esMascota', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=20)),
                ('nombre', models.CharField(max_length=20)),
                ('modelo', models.IntegerField()),
                ('esEcofriendly', models.BooleanField()),
            ],
        ),
    ]