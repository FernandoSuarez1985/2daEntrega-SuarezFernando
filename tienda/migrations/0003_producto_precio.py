# Generated by Django 4.0.4 on 2023-01-09 20:27

from django.db import migrations, models



class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_producto_created_producto_updated_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='precio',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]