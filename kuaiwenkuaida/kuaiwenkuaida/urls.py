from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'kuaiwenkuaida.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$','App.views.index',name='index'),
    url(r'^tiwen/$','App.views.tiwen',name='tiwen'),
    url(r'^saveQuestion$','App.views.saveQuestion',name='saveQuestion'),
)
