# Generated by Django 4.1.2 on 2023-07-13 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0003_producto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes', verbose_name='imagen'),
        ),
    ]
