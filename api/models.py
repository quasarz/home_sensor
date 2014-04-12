from django.db import models

class SensorNode(models.Model): 
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    created = models.DateTimeField()
