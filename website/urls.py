from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^program', views.program, name='program'),
    url(r'^list', views.list, name='list'),
    url(r'^faculty', views.faculty, name='faculty'),
    url(r'^research', views.research, name='research'),
    url(r'^contactus', views.contactus, name='contactus'),
    url(r'^outreach', views.outreach, name='outreach'),
    url(r'^Outreaches/(?P<pk>\d+)$', views.item_outreach, name='outreach_item'),
    url(r'^news', views.news, name='news'),
    url(r'^News/(?P<pk>\d+)$', views.news_item, name='news_item'),
    url(r'^education', views.education, name='education'),
    url(r'^business', views.business, name='business'),
    url(r'^administration', views.administration, name='administration'),
    url(r'^management', views.management, name='management'),
    url(r'^computer_studies', views.computer_studies, name='computer_studies'),
    url(r'^criminal_justice', views.criminal_justice, name='criminal_justice'),
    url(r'^psychology', views.psychology, name='psychology'),
    url(r'^nursing', views.nursing, name='nursing'),
    url(r'^content_news', views.contactus, name='content_news'),
    url(r'^content_outreach', views.contactus, name='content_outreach'),
    url(r'^content_research', views.contactus, name='content_research'),
    url(r'^Programs/(?P<pk>\d+)$', views.program_item, name='program_item'),
]