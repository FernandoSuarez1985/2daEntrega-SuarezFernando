# Generated by Django 4.0.4 on 2023-01-10 20:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0003_producto_precio'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoriaprod',
            options={'verbose_name': 'CategoriaProd', 'verbose_name_plural': 'CategoriasProd'},
        ),
        migrations.RemoveField(
            model_name='producto',
            name='precio',
        ),
    ]
