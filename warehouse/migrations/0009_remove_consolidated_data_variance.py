# Generated by Django 2.1.7 on 2019-02-19 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0008_auto_20190219_1739'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consolidated_data',
            name='variance',
        ),
    ]
