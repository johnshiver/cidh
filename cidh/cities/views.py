from django.shortcuts import render
from django.views.generic import View

# Create your views here.

from .models import City


class Home(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):

        cities = City.objects.all()
        return render(request, self.template_name, {'cities': cities})


class cityView(View):
    template_name = 'city.html'

    def get(self, request, *args, **kwargs):
        pass
