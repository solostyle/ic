from django.conf.urls import patterns, include, url

# the next two lines enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('therapy.views',
    # Examples:
    # url(r'^$', 'icare.views.home', name='home'),
    # url(r'^icare/', include('icare.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^exercises/$', 'index'),
    url(r'^exercises/(?P<exercise_id>\d+)/$', 'detail'),
    url(r'^exercises/(?P<exercise_id>\d+)/joints/$', 'joints'),
    url(r'^exercises/(?P<exercise_id>\d+)/categories/$', 'categories')
)
urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
)
