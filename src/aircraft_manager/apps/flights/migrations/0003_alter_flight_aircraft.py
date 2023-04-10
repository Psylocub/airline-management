# Generated by Django 4.1.6 on 2023-02-13 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("aircrafts", "0002_alter_aircraft_manufacturer_and_more"),
        ("flights", "0002_alter_flight_options_alter_flight_unique_together"),
    ]

    operations = [
        migrations.AlterField(
            model_name="flight",
            name="aircraft",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="aircrafts.aircraft",
            ),
        ),
    ]