from django.conf.urls import patterns, include, url

# the next two lines enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'icare.views.home', name='home'),
    # url(r'^icare/', include('icare.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^exercises/$', 'therapy.views.index'),
    url(r'^exercises/(?P<exercise_id>\d+)/$', 'therapy.views.detail'),
    url(r'^exercises/(?P<exercise_id>\d+)/joints/$', 'therapy.views.joints'),
    url(r'^exercises/(?P<exercise_id>\d+)/categories/$', 'therapy.views.categories')
)
