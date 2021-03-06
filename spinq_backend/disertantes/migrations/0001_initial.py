# Generated by Django 2.1.2 on 2018-10-02 19:27

from django.db import migrations, models
import django.db.models.deletion
import versatileimagefield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
        ('charlas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disertante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
                ('bio', models.TextField(blank=True, null=True)),
                ('pic', versatileimagefield.fields.VersatileImageField(blank=True, null=True, upload_to='users/pics')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('spinq_user_admin', models.ForeignKey(blank=True, help_text='Usuario que administra el perfil', null=True, on_delete=django.db.models.deletion.SET_NULL, to='usuarios.SpinqUser')),
            ],
        ),
        migrations.CreateModel(
            name='DisertanteEnCharla',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('charla', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='charlas.Charla')),
                ('disertante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='disertantes.Disertante')),
                ('spinq_user_added', models.ForeignKey(blank=True, help_text='Usuario que lo cargo', null=True, on_delete=django.db.models.deletion.SET_NULL, to='usuarios.SpinqUser')),
            ],
        ),
    ]
