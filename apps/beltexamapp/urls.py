from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^validation$', views.validation),
    url(r'^login$', views.login),
    url(r'^welcome$', views.welcome),
    url(r'^add_item$', views.add_item),
    url(r'^add$', views.add),
    url(r'^create$', views.create),
    url(r'^home$', views.home),
    url(r'^logout$', views.logout),
]
