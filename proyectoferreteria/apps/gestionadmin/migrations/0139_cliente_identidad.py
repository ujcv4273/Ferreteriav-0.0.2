# Generated by Django 2.2.6 on 2020-06-24 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionadmin', '0138_auto_20200624_2001'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='Identidad',
            field=models.CharField(default=123, max_length=13, verbose_name='Identidad del Cliente'),
            preserve_default=False,
        ),
    ]
