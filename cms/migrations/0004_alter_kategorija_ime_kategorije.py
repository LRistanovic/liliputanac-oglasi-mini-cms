# Generated by Django 4.0.1 on 2022-01-22 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_grad_alter_oglas_grad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kategorija',
            name='ime_kategorije',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
