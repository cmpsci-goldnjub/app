from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from project.teams.models import Team

import hashlib
import os
import uuid


def get_file_dir(instance, filename):
    return os.path.join(str(instance.pk), filename)


class VideoSubmission(models.Model):

    class Meta:
        ordering = ['-created']
        get_latest_by = "created"

    team = models.ForeignKey(Team, blank=True, null=True, on_delete=models.SET_NULL)
    submitter = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    created = models.DateTimeField(auto_now_add=True)
    video_url = models.URLField()

    def __str__(self):
        return self.team.name


class FileSubmission(models.Model):

    class Meta:
        ordering = ['-created']
        get_latest_by = "created"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    team = models.ForeignKey(Team, blank=True, null=True, on_delete=models.SET_NULL)
    submitter = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    created = models.DateTimeField(auto_now_add=True)
    submission = models.FileField(upload_to=get_file_dir)
    comments = models.TextField(blank=True, validators=[MaxLengthValidator(1000)],
                                help_text="Any last-minute comments? Don't forget you need README!")
    md5sum = models.CharField(max_length=32, blank=True)

    def __str__(self):
        return self.team.name


@receiver(post_save, sender=FileSubmission)
def file_submission_post_save(sender, instance, **kwargs):
    """Called after a FileSubmission is saved
    - Sets the file's MD5 sum if it isn't already set
    """

    if not instance.md5sum:
        filehash = hashlib.md5()
        with open(instance.submission.path) as f:
            for chunk in iter(lambda: f.read(4096), ""):
                filehash.update(chunk)
        instance.md5sum = filehash.hexdigest()
        instance.save()
