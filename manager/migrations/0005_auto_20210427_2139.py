# Generated by Django 3.2 on 2021-04-28 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0004_alter_maneger_cpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maneger',
            name='birthday',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='maneger',
            name='cpf',
            field=models.CharField(max_length=11, unique=True),
        ),
    ]
