from django.db import models

# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=10)
    drink_legal = models.BooleanField()

    def __str__(self):
        return '%s, %s' % (self.name, self.country)
