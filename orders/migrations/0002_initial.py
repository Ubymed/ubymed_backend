# Generated by Django 4.2.6 on 2023-10-21 02:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("orders", "0001_initial"),
        ("services", "0001_initial"),
        ("partners", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="ordenconsultamedica",
            name="catalogo_consulta",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="services.consultamedica",
            ),
        ),
        migrations.AddField(
            model_name="ordenconsultamedica",
            name="orden_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="orders.orden"
            ),
        ),
        migrations.AddField(
            model_name="ordenconsultamedica",
            name="socio",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="partners.socio"
            ),
        ),
        migrations.AddField(
            model_name="orden",
            name="usuario",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="detalleordenlaboratorio",
            name="catalogo_prueba_laboratorio",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="services.pruebalaboratorio",
            ),
        ),
        migrations.AddField(
            model_name="detalleordenlaboratorio",
            name="orden_laboratorio",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="orders.ordenpruebalaboratorio",
            ),
        ),
    ]
