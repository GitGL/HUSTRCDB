from django.conf.urls import patterns, url

from projectors import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^Build/$', views.builds, name='builds'),
    url(r'^Build/(?P<build_id>\d+)/$', views.build_rooms, name='rooms'),
    url(r'^Brand/$', views.brands, name='brands'),
    url(r'^Brand/(?P<brand_id>\d+)/$', views.brand_projector, name='brand_projector'),
    url(r'^Projector/$', views.projectors, name='projectors'),
    url(r'^Projector/(?P<projector_id>\d+)/State/$', views.status_records, name='status_records'),
    url(r'^Projector/(?P<projector_id>\d+)/Maintenance/$', views.maintenance_records, name='maintenance_records'),
	url(r'^Projector/(?P<projector_id>\d+)/Problem/$', views.projector_problems, name='projector_problems'),
	url(r'^Projector/(?P<projector_id>\d+)/Problem/add/$', views.add_problem, name='add_problem')
)
