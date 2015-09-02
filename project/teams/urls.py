"""
project.teams URL Configuration

"""
from django.conf.urls import url

from .views import TeamListView

urlpatterns = [
    url(r'^$', TeamListView.as_view())
]
