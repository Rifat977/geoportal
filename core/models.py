from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.db.models import JSONField



class Country(models.Model):
    name_common = models.CharField(max_length=100)
    name_official = models.CharField(max_length=255)
    cca2 = models.CharField(max_length=3)
    cca3 = models.CharField(max_length=3)
    cioc = models.CharField(max_length=3, null=True, blank=True)
    region = models.CharField(max_length=100)
    subregion = models.CharField(max_length=100, null=True, blank=True)
    capital = ArrayField(models.CharField(max_length=100), blank=True, null=True)
    area = models.FloatField()
    population = models.BigIntegerField()
    timezones = ArrayField(models.CharField(max_length=50))
    flag_emoji = models.CharField(max_length=10)
    flag_png = models.URLField(max_length=500, null=True, blank=True)
    flag_svg = models.URLField(max_length=500, null=True, blank=True)
    borders = ArrayField(models.CharField(max_length=3), blank=True, null=True)
    languages = JSONField()
    currencies = JSONField()
    maps_google = models.URLField(null=True, blank=True)
    maps_osm = models.URLField(null=True, blank=True)
    landlocked = models.BooleanField(default=False)
    tlds = ArrayField(models.CharField(max_length=10), blank=True, null=True)

    def __str__(self):
        return self.name_common
