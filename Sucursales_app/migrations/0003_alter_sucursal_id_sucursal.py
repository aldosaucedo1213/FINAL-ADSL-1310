# Generated by Django 5.1 on 2024-11-29 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sucursales_app', '0002_alter_sucursal_id_sucursal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sucursal',
            name='id_sucursal',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
