from django.conf.urls import include, url

from . import views


urlpatterns = [
    url('^$', views.index, name='index'),
    url(r'^ajax/add/$', views.add_todo, name='add_todo'),
    url(r'^ajax/status/$', views.change_status, name='change_status'),
    url(r'^ajax/delete-completed/$', views.del_completed, name='del_completed'),
    url(r'^ajax/delete-all/$', views.del_all, name='del_all'),
]
