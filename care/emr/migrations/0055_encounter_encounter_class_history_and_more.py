# Generated by Django 5.1.3 on 2024-12-28 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emr', '0054_tokenbooking_encounter_appointment'),
    ]

    operations = [
        migrations.AddField(
            model_name='encounter',
            name='encounter_class_history',
            field=models.JSONField(default=dict),
        ),
        migrations.AddField(
            model_name='encounter',
            name='status_history',
            field=models.JSONField(default=dict),
        ),
    ]