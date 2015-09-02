"""
project URL Configuration

"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin_tools/', include('admin_tools.urls')),

    url(r'^accounts/logout/$', 'allauth.account.views.logout', name='account_logout'),
    url('^accounts/social/', include('allauth.socialaccount.urls')),
    url('^accounts/', include('allauth.socialaccount.providers.google.urls')),

    url(r'^', include("project.teams.urls")),
    url(r'^', include("project.profiles.urls")),
]
