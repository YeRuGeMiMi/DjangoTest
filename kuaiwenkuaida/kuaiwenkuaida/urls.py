from django.conf.urls import patterns, include, url

from django.contrib import admin
# import captcha

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'kuaiwenkuaida.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$','App.views.index',name='index'),
    url(r'^tiwen$','App.views.tiwen',name='tiwen'),
    url(r'^huida/$','App.views.huida',name='huida'),
    #url(r'^saveQuestion$','App.views.saveQuestion',name='saveQuestion'),
    url(r'^ajax/qustion','App.views.ajaxReturn',name='ajaxReturn'),
    url(r'^reg/answer$','App.views.regAnswer',name='regAnswer'),
    #url(r'^captcha/$',include('captcha.urls')),
)
