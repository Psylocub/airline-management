# Generated by Django 4.1.6 on 2023-02-10 00:04

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("aircrafts", "0002_alter_aircraft_manufacturer_and_more"),
        ("flights", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="flight",
            options={},
        ),
        migrations.AlterUniqueTogether(
            name="flight",
            unique_together={("aircraft", "is_active")},
        ),
    ]