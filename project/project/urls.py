"""
project URL Configuration

"""
from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from django.views.generic.base import RedirectView


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin_tools/', include('admin_tools.urls')),

    url(r'^accounts/login/$', RedirectView.as_view(url=settings.LOGIN_URL),
        name='account_login'),
    url(r'^accounts/logout/$', 'allauth.account.views.logout', name='account_logout'),
    url(r'^accounts/social/', include('allauth.socialaccount.urls')),
    url(r'^accounts/', include('allauth.socialaccount.providers.google.urls')),

    url(r'^', include("project.teams.urls")),
    url(r'^', include("project.profiles.urls")),
]
