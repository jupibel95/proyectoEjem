# Generated by Django 3.1.3 on 2020-11-26 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Centro_asistencial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=64)),
                ('nit', models.IntegerField()),
                ('numero_de_camas_en_uci', models.IntegerField(max_length=10)),
                ('numero_de_camas_ocupadas_en_uci', models.IntegerField(max_length=10)),
                ('numero_de_camas_disponibles_en_uci', models.IntegerField(max_length=10)),
            ],
        ),
    ]
