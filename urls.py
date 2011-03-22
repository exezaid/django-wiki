from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^wiki/', include('wiki.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),

    (r'^wiki/(?<page_name>[^/]+)/edit/', 'wiki.views.edit_page'),
    (r'^wiki/(?<page_name>[^/]+)/save/', 'wiki.views.save_page'),
    (r'^wiki/(?<page_name>[^/]+)/', 'wiki.views.view_page'),
)

import sys, os
from django.conf import settings
if 'runserver' in sys.argv or 'runserver_plus':
    urlpatterns = patterns('', url(r'^media/(.*)$', 'django.views.static.serve',
        kwargs={'document_root': settings.MEDIA_ROOT}),
    ) + urlpatterns
