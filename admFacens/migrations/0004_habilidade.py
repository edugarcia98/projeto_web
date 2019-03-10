# Generated by Django 2.1.7 on 2019-03-10 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admFacens', '0003_competencia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habilidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Habilidade')),
                ('description', models.CharField(max_length=1000, verbose_name='Descricao')),
            ],
            options={
                'ordering': ('title',),
            },
        ),
    ]
