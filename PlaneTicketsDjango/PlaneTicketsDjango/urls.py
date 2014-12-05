from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
import views
#from django.views.generic.base import TemplateView

urlpatterns = patterns('',
    url(r'^home/', 'PlaneTicketsDjango.views.index', name = 'index'),
    url(r'^displayIndex/', views.index),
    url(r'^displayDetails/(?P<indexnum>\d+)', views.details, name='detail'),
    url(r'^displayInfo/', views.displayInfo),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^home/', TemplateView.as_view(template_name='index.html')),
)
