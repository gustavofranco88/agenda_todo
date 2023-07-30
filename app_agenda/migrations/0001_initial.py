# Generated by Django 4.2.3 on 2023-07-30 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('data', models.DateTimeField(verbose_name='Data')),
                ('data_criacao', models.DateTimeField(auto_now=True, verbose_name='Criado em')),
            ],
            options={
                'db_table': 'evento',
            },
        ),
    ]
