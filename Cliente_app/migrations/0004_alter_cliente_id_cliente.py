# Generated by Django 5.1 on 2024-11-29 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cliente_app', '0003_alter_cliente_id_cliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='id_cliente',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]