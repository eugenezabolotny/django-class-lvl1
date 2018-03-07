from django.conf.urls import include, url

from . import views


urlpatterns = [
    url('^$', views.index, name='index'),
    url(r'^ajax/add/$', views.add_todo, name='add_todo')
]
