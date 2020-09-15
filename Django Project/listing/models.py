from django.db import models


# Create your models here.
class Carlisting(models.Model):
    title = models.CharField(max_length=100)
    model = models.CharField(max_length=20)
    engine_cc = models.IntegerField()
    color = models.CharField(max_length=100)
    car_type = models.CharField(max_length=20)
    passenger_capacity = models.CharField(max_length=50)
    gear = models.CharField(max_length=50)
    manufacture_year = models.IntegerField()
    price = models.IntegerField()
    Car_image = models.ImageField(upload_to='photos/%Y/%m/%d/',default = None)

    def __str__(self):
        return self.title
