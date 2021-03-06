from django.db import models

# Create your models here.


class City(models.Model):
    city = models.CharField(max_length=50)
    geography = models.CharField(max_length=50, null=True)
    jurisdiction = models.CharField(max_length=256, null=True)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=100)
    drink_legal = models.BooleanField(default=None)
    park = models.BooleanField(default=None)
    park_info = models.TextField(default=None)
    street = models.BooleanField(default=None)
    street_info = models.TextField(default=None)
    vehicle = models.BooleanField(default=None)
    vehicle_info = models.TextField(default=None)
    transportation = models.BooleanField(default=None)
    transportation_info = models.TextField(default=None)
    beer = models.CharField(max_length=50, default=None)
    wine = models.CharField(max_length=50, default=None)
    liquor = models.CharField(max_length=50, default=None)
    age = models.CharField(max_length=256)
    hours = models.CharField(max_length=256, null=True)

    cta1_url = models.CharField(max_length=256, default='foo', blank=True, null=True)
    cta1_title = models.CharField(max_length=256, default='foo', blank=True, null=True)
    cta2_url = models.CharField(max_length=256, default='foo', blank=True, null=True)
    cta2_title = models.CharField(max_length=256, default='foo', blank=True, null=True)
    cta3_url = models.CharField(max_length=256, default='foo', blank=True, null=True)
    cta3_title = models.CharField(max_length=256, default='foo', blank=True, null=True)
    cta4_url = models.CharField(max_length=256, default='foo', blank=True, null=True)
    cta4_title = models.CharField(max_length=256, default='foo', blank=True, null=True)
    cta5_url = models.CharField(max_length=256, default='foo', blank=True, null=True)
    cta5_title = models.CharField(max_length=256, default='foo', blank=True, null=True)

    def __str__(self):
        return '%s, %s' % (self.city, self.country)
