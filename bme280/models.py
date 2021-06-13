from django.db import connections
from django.db import models

class Bme280(models.Model):   
    date = models.DateField()
    temperature = models.FloatField()
    pressure = models.FloatField()

    humidity = models.FloatField()
    class Meta:
        db_table = "PME280"