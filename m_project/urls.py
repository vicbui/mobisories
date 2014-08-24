from django.conf.urls import patterns, include, url
from mobisories import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', include('mobisories.urls'), name='index'),
    #url(r'^admin/', include(admin.site.urls)),
)
