# Generated by Django 2.2.4 on 2020-08-12 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_consumerdetails_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consumer_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=6)),
                ('address', models.CharField(max_length=30)),
                ('contact', models.IntegerField()),
                ('con_email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=20)),
                ('photo', models.ImageField(upload_to='consumer_photo/')),
            ],
        ),
        migrations.DeleteModel(
            name='ConsumerDetails',
        ),
    ]