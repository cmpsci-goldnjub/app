from django.contrib import admin

from .models import FileSubmission, VideoSubmission


class FileSubmissionInline(admin.TabularInline):
    model = FileSubmission


class VideoSubmissionInline(admin.TabularInline):
    model = VideoSubmission


@admin.register(FileSubmission)
class FileSubmissionAdmin(admin.ModelAdmin):
    model = FileSubmission
    list_display = ('team', 'submitter', 'created')


@admin.register(VideoSubmission)
class VideoSubmissionAdmin(admin.ModelAdmin):
    model = VideoSubmission
    list_display = ('team', 'submitter', 'created')
