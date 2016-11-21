from django.conf import settings
from django.conf.urls import include, url
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    url (r'^$', views.room_list),
    url (r'^room/(?P<room_pk>[0-9]+)/new$', views.send_message, name ='new_message'),
    url (r'^room/(?P<room_pk>[0-9]+)/$', views.view_messages, name ='view_messages'),
]
