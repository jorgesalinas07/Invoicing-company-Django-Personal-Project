# Generated by Django 4.0.2 on 2022-02-26 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoicing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='nit',
            field=models.PositiveIntegerField(max_length=10, unique=True),
        ),
    ]
