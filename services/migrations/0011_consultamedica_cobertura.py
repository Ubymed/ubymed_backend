# Generated by Django 4.2.7 on 2023-11-25 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0010_consultamedica_tiempo_estimado'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultamedica',
            name='cobertura',
            field=models.CharField(default='Ciudad de Guatemala'),
            preserve_default=False,
        ),
    ]
