from django.conf.urls import patterns, include, url
from django.contrib import admin
from cities.views import Home

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', Home.as_view(), name='home'),
)
