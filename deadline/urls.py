from django.conf.urls import patterns, include, url
from django.contrib import admin
from website import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'deadline.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index)
)
