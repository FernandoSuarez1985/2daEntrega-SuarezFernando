# Generated by Django 4.0.4 on 2023-01-10 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0011_alter_categoriaprod_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='precio',
        ),
    ]
