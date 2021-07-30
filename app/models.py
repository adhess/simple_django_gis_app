from django.db import models


class Provider(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    currency = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ServiceArea(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=12, decimal_places=3)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Coordinate(models.Model):
    lat = models.FloatField()
    lng = models.FloatField()
    service_area = models.ForeignKey(ServiceArea, on_delete=models.CASCADE)

