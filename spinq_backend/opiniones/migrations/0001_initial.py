# Generated by Django 2.1.2 on 2018-10-02 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
        ('charlas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaOpinion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
                ('mas_es_bueno', models.BooleanField(default=True, null=True)),
                ('maximo', models.IntegerField(default=4, help_text='Maximo valor de la valoracion posible. Si es 1 entonces solo podes elegir pulgar arriba o abajo. Si son 5 pueden ser estrellas por ejemplo')),
                ('default_value', models.IntegerField(default=2, help_text='Valor predeterminado al mostrarse a los usuarios')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Opinion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anonima', models.BooleanField(default=True)),
                ('valoracion', models.IntegerField()),
                ('observaciones', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opiniones.CategoriaOpinion')),
                ('charla', models.ForeignKey(blank=True, help_text='Vacío si esta opinando en general del disertante', null=True, on_delete=django.db.models.deletion.SET_NULL, to='charlas.Charla')),
                ('spinq_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.SpinqUser')),
            ],
        ),
    ]
