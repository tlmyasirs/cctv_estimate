from django.db import models

class Cam(models.Model):
    name = models.CharField(max_length=50)
    mp = models.DecimalField(max_digits=3, decimal_places=0)
    price = models.DecimalField(max_digits=5, decimal_places=2)

class Nvr(models.Model):
    name = models.CharField(max_length=50)
    ch = models.DecimalField(max_digits=3,decimal_places=0)
    price = models.DecimalField(max_digits=5, decimal_places=2)

class Hdd(models.Model):
    name = models.CharField(max_length=50)
    size = models.DecimalField(max_digits=3, decimal_places=0)
    price = models.DecimalField(max_digits=5, decimal_places=2)


