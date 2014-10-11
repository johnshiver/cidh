from django.contrib import admin

from .models import City


class CityAdmin(admin.ModelAdmin):

    fields = ('city',
              'geography',
              'jurisdiction',
              'state',
              'country',
              'drink_legal',
              'park',
              'park_info',
              'street',
              'street_info',
              'vehicle',
              'vehicle_info',
              'transportation',
              'transportation_info',
              'beer',
              'wine',
              'liquor',
              'age',
              'hours',)


admin.site.register(City, CityAdmin)
