from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^program' , views.program, name='program'),
    url(r'^list', views.list, name='list'),
    url(r'^research' , views.research, name='research'),
    url(r'^contactus', views.contactus, name='contactus'),
    url(r'^outreach' , views.outreach, name='outreach'),
    url(r'^news' , views.news, name='news'),
    url(r'^content_news', views.contactus, name='content_news'),
    url(r'^content_outreach', views.contactus, name='content_outreach'),
    url(r'^content_research', views.contactus, name='content_research'),
]