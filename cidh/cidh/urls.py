from django.conf.urls import patterns, include, url
from django.contrib import admin

# from django.conf import settings
# from django.conf.urls.static import static

from cities.views import Home, cityView, cityDetailView

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', Home.as_view(), name='home'),
    url(r'^city/(?P<city_id>\d+)/$', cityView.as_view(), name='city_view'),
    url(r'^city_detail/(?P<city_id>\d+)/$', cityDetailView.as_view(), name='city_view')
)

# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
