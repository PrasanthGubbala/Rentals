# Generated by Django 2.2.4 on 2020-08-12 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200812_1548'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConsumerDetails',
            fields=[
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=6)),
                ('contact', models.IntegerField()),
                ('con_email', models.EmailField(max_length=254, primary_key=True, serialize=False, unique=True)),
                ('address', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to='consumer_photo/')),
            ],
        ),
    ]
