# Generated by Django 2.1.7 on 2019-04-06 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admFacens', '0003_auto_20190406_0845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objetivo',
            name='curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='objetivos', to='admFacens.Curso'),
        ),
    ]