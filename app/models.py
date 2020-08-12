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
    service_id = models.AutoField(primary_key=True)
    service_type = models.CharField(max_length=20)
    rooms = models.IntegerField()
    square_feets = models.IntegerField()
    price = models.IntegerField()
    city = models.CharField(max_length=30)
    area = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    door_no = models.CharField(max_length=15,unique=True)
    image = models.ImageField(upload_to='services/')
