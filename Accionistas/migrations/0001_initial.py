# Generated by Django 4.1 on 2022-12-17 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accionista',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('rut', models.CharField(max_length=10)),
                ('observacion', models.IntegerField(max_length=10)),
                ('fecha_asociacion', models.DateField()),
                ('activo', models.BooleanField()),
                ('monto', models.IntegerField()),
            ],
        ),
    ]
