"""
project. URL Configuration

"""
from django.conf.urls import url

from .views import (submission_list_view,
                    submission_submit_video,
                    submission_submit_file)

urlpatterns = [
    url(r'^submissions/$', submission_list_view, name="submission_list"),
    url(r'^submit-video/$', submission_submit_video, name="submit_video"),
    url(r'^submit-file/$', submission_submit_file, name="submit_file"),
]
