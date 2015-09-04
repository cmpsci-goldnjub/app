"""
project.profiles URL Configuration

"""
from django.conf.urls import url

from .views import (profile_list_view,
                    profile_detail_view,
                    profile_update_view)


urlpatterns = [
    url(r'^profiles/$', profile_list_view, name="profile_list"),
    url(r'^profiles/update/$', profile_update_view, name="profile_update"),
    url(r'^profile/(?P<username>[\w.@+-]+)/$', profile_detail_view, name="profile_detail"),
]
