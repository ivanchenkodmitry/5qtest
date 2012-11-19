from devotional.views import get_devotional, get_devotionals_count, get_devotional_with_count
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'test_project.views.home', name='home'),
    # url(r'^test_project/', include('test_project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^get_devotional/(?P<month>\d+)/(?P<day>\d+)/$', get_devotional, name='det_devotional'),
    url(r'^get_devotional/(?P<month>\d+)/(?P<day>\d+)/count/$', get_devotional_with_count),
    url(r'^devotional_words_count/$', get_devotionals_count)

)
