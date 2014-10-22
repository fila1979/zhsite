from django.conf.urls import patterns, include, url
from django.contrib import admin
from zhapp.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'zhsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', index),
    url(r'^index/', index),
    url(r'^about/', about),
    url(r'^contacts/', contacts),
    url(r'^product/', product),
    url(r'^projects/', projects),
    url(r'^admin/', include(admin.site.urls)),

    # develop static

    url('^static/$', 'django.views.static.serve',
        {'document_root': '/zhsite/static/'}
        )


)
