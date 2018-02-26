from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^heatmap', views.heatmap, name='index'),
    url(r'^searchbus', views.searchbus, name='index'),
    url(r'^numofeverday', views.numofeverday, name='index'),
    url(r'^numofhour', views.numofhour_sum, name='index'),
    url(r'^heatofhoureverday', views.numofhour_everday, name='index'),
    url(r'^locwithtime', views.locationwithtime, name='index'),
    url(r'^pieofmes', views.pieofmes, name='index'),
    url(r'^num', views.num, name='index')
]

