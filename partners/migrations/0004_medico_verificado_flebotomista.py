# Generated by Django 4.2.6 on 2023-10-21 02:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("partners", "0003_remove_medico_especialidad"),
    ]

    operations = [
        migrations.AddField(
            model_name="medico",
            name="verificado",
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name="Flebotomista",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("verificado", models.BooleanField(default=False)),
                ("online", models.BooleanField(default=False)),
                (
                    "socio",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="partners.socio"
                    ),
                ),
            ],
        ),
    ]
