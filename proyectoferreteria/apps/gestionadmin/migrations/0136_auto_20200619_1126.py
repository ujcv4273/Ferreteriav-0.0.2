# Generated by Django 2.2.6 on 2020-06-19 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionadmin', '0135_auto_20200618_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comprasenc',
            name='fecha_factura',
            field=models.DateField(blank=True, default='2020-06-20', null=True),
        ),
    ]