from django.conf.urls import patterns, url

urlpatterns = patterns('simpleavatar.views',
    url('^change/$', 'change', name='avatar_change'),
)
