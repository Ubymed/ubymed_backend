# Generated by Django 4.2.6 on 2023-10-30 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_alter_usuario_managers"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usuario",
            name="sexo",
            field=models.CharField(
                choices=[("m", "Masculino"), ("f", "Femenino")],
                default="f",
                max_length=1,
            ),
        ),
    ]