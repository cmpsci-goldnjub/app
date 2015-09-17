from django.contrib import admin

from project.submission.admin import FileSubmissionInline, VideoSubmissionInline

from .models import Team, Request


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    model = Team
    filter_horizontal = ('members',)
    inlines = (FileSubmissionInline, VideoSubmissionInline)


@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    model = Request
