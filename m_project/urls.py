from django.conf.urls import patterns, include, url
from mobisories import views
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', include('mobisories.urls')),
    
)

if settings.DEBUG:
	urlpatterns += patterns(
		'django.views.static',
		(r'media/(?P<path>.*)',
		'serve',
		{'document_root':settings.MEDIA_ROOT}), )



