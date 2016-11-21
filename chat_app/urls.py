from django.conf import settings
from django.conf.urls import include, url
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    url (r'^$', views.room_list),
]
