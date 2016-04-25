from django.conf.urls import patterns, include, url
from django.contrib import admin

# from my_app import polls

import polls

from polls.resource import DataResource
from tastypie.api import Api

v1_api = Api(api_name='v1')
v1_api.register(DataResource())


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'polls.views.home', name='home'),
    (r'^', include(v1_api.urls)),

    url(r'^admin/', include(admin.site.urls)),
)
