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
        if current_city.cta1_url != 'foo':
            url1 = current_city.cta1_url
        else:
            url1 = None
        if current_city.cta2_url != 'foo':
            url2 = current_city.cta2_url
        else:
            url2 = None
        if current_city.cta3_url != 'foo':
            url3 = current_city.cta3_url
        else:
            url3 = None

        return render(request, self.template_name, {'city': current_city,
                                                    'url1': url1,
                                                    'url2': url2,
                                                    'url3': url3})


class cityDetailView(View):
    template_name = 'city_detail.html'

    def get(self, request, *args, **kwargs):
        city_id = int(self.kwargs['city_id'])
        current_city = City.objects.get(pk=city_id)
        return render(request, self.template_name, {'city': current_city})


class disclaimerView(View):
    template_name = 'disclaimer.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
