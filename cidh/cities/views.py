from django.shortcuts import render
from django.views.generic import View

# Create your views here.

from .models import City


class Home(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):

        cities = City.objects.order_by('city').all()
        return render(request, self.template_name, {'cities': cities})


class cityView(View):
    template_name = 'city.html'

    def get(self, request, *args, **kwargs):
        city_id = int(self.kwargs['city_id'])
        current_city = City.objects.get(pk=city_id)

        return render(request, self.template_name, {'city': current_city})


class cityDetailView(View):
    template_name = 'city_detail.html'

    def get(self, request, *args, **kwargs):
        city_id = int(self.kwargs['city_id'])
        current_city = City.objects.get(pk=city_id)
        return render(request, self.template_name, {'city': current_city})
