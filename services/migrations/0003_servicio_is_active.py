# Generated by Django 4.2.6 on 2023-10-22 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0002_servicio"),
    ]

    operations = [
        migrations.AddField(
            model_name="servicio",
            name="is_active",
            field=models.BooleanField(default=False),
        ),
    ]
