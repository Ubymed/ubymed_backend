# Generated by Django 4.2.6 on 2023-10-22 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0003_remove_registroconsultamedica_orden_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="orden",
            name="estado",
            field=models.CharField(
                choices=[
                    ("incompleta", "Incompleta"),
                    ("completa", "Completa"),
                    ("cancelada", "Cancelada"),
                ],
                default="incompleta",
            ),
        ),
        migrations.AlterField(
            model_name="orden",
            name="tipo",
            field=models.CharField(
                choices=[
                    ("consulta_medica", "Consulta Médica"),
                    ("prueba_laboratorio", "Prueba de Laboratorio"),
                ]
            ),
        ),
    ]
