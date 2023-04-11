# Generated by Django 4.0.4 on 2023-01-09 20:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0007_rename_price_producto_precio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='precio',
        ),
        migrations.AddField(
            model_name='producto',
            name='precios',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]