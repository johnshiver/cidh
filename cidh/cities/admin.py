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
              'hours',
              'cta1_url',
              'cta1_title',
              'cta2_url',
              'cta2_title',
              'cta3_url',
              'cta3_title',
              'cta4_url',
              'cta4_title',
              'cta5_url',
              'cta5_title',
              )


admin.site.register(City, CityAdmin)
