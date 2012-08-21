from django.conf.urls import patterns, include, url

urlpatterns = patterns('therapy.views',
	url(r'^$', 'index'),
    	url(r'^(?P<exercise_id>\d+)/$', 'detail'),
	url(r'^(?P<exercise_id>\d+)/joints/$', 'joints'),
	url(r'^(?P<exercise_id>\d+)/categories/$', 'categories')
)
