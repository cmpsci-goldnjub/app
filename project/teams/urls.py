"""
project.teams URL Configuration

"""
from django.conf.urls import url

from .views import (team_list_view,
                    team_detail_view,
                    team_create_view,
                    team_leave_view,
                    team_update_view,
                    request_send_view,
                    request_response_view)

urlpatterns = [
    url(r'^teams/$', team_list_view, name="team_list"),
    url(r'^teams/create/$', team_create_view, name="team_create"),
    url(r'^teams/update/$', team_update_view, name="team_update"),
    url(r'^teams/leave/$', team_leave_view, name="team_leave"),
    url(r'^team/(?P<slug>[-\w]+)/$', team_detail_view, name="team_detail"),
    url(r'^team/(?P<slug>[-\w]+)/request/$', request_send_view, name="request_send"),

    url(r'^request/(?P<pk>\d+)/$', request_response_view, name="request_response"),
]
