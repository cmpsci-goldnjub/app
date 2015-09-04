from django.contrib import admin

from .models import Team, Request


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    model = Team
    filter_horizontal = ('members',)

@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    model = Request
