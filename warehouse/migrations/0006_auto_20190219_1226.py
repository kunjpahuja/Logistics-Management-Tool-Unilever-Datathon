# Generated by Django 2.1.7 on 2019-02-19 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0005_obdb'),
    ]

    operations = [
        migrations.RenameField(
            model_name='obdb',
            old_name='costCounter',
            new_name='costCenter',
        ),
    ]