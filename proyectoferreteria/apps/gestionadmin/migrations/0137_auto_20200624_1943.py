# Generated by Django 2.2.6 on 2020-06-24 19:43

from django.db import migrations, models
import proyectoferreteria.apps.gestionadmin.models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionadmin', '0136_auto_20200619_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='Precio_Compra',
            field=models.FloatField(validators=[proyectoferreteria.apps.gestionadmin.models.validarquenoseacero], verbose_name='Precio Compra'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='Precio_Venta',
            field=models.FloatField(validators=[proyectoferreteria.apps.gestionadmin.models.validarquenoseacero], verbose_name='Precio Venta'),
        ),
    ]
