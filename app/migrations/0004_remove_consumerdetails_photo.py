# Generated by Django 2.2.4 on 2020-08-12 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_consumerdetails'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consumerdetails',
            name='photo',
        ),
    ]