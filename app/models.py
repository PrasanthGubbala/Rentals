from django.db import models

class ProviderDetails(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=6)
    contact = models.IntegerField(unique=True)
    address = models.TextField()
    email = models.EmailField(unique=True,primary_key=True)
    password = models.CharField(max_length=30)
    photo = models.ImageField(upload_to='provider_photo')

class Services(models.Model):
    s_id = models.AutoField(primary_key=True)
    email = models.EmailField()
    service_type = models.CharField(max_length=20)
    rooms = models.IntegerField()
    square_feets = models.IntegerField()
    price = models.FloatField()
    city = models.CharField(max_length=30)
    area = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    door_no = models.CharField(unique=True,max_length=15)
    image = models.ImageField(upload_to='services/')

class ConsumerDetails(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    gender = models.CharField(max_length=6)
    address = models.CharField(max_length=30)
    contact = models.IntegerField()
    con_email = models.EmailField(unique=True,primary_key=True)
    password = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='consumer_photo/')