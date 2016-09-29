from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<requester>[\w\-]+)/$', views.check_requester, name='requester'),
    url(r'^timetable/(?P<requester>[\w\-]+)/$', views.timetable, name='timetable'),
    url(r'^classes/(?P<classes_id>[\w\-]+)/$', views.classes, name='classes'),
    url(r'^subject/(?P<subject_name>[\w\-]+)/(?P<classes_id>[0-9]+)/$', views.subject_wise_mark, name='subject'),
]