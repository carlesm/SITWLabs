from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()


from isobres.views import *


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sobres.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', mainpage, name='home'),
    url(r'^admin/', include(admin.site.urls)),
)