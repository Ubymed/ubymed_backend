# Generated by Django 4.2.6 on 2023-10-22 01:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0003_servicio_is_active"),
        ("orders", "0005_alter_orden_tipo"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="orden",
            name="tipo",
        ),
        migrations.AddField(
            model_name="orden",
            name="servicio",
            field=models.ForeignKey(
                default=0,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="services.servicio",
            ),
            preserve_default=False,
        ),
    ]
