# Generated by Django 2.1.7 on 2019-03-16 17:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admFacens', '0005_auto_20190316_1359'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Disciplina')),
                ('tipo', models.CharField(choices=[('T', 'Teorica'), ('P', 'Pratica')], max_length=1, verbose_name='Tipo')),
                ('creditos', models.IntegerField(validators=[django.core.validators.MinValueValidator(2), django.core.validators.MaxValueValidator(8)], verbose_name='Creditos')),
            ],
            options={
                'ordering': ('title',),
            },
        ),
    ]
