# Generated by Django 4.0.4 on 2023-01-09 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0006_rename_precio_producto_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='price',
            new_name='precio',
        ),
    ]
