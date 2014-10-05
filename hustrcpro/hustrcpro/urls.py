from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

#import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hustrcpro.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)), 
    url(r'^projectors/', include('projectors.urls', namespace='projectors')),
)

