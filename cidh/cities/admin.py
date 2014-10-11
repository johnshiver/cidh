from django.contrib import admin

from .models import City


class CityAdmin(admin.ModelAdmin):

    fields = ('name',
              'country',
              'is_legal')


admin.site.register(City, CityAdmin)
