from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^rajeunir$', views.rajeunir, name='rajeunir'),
    url(r'^liste$', views.liste, name='liste'),
]
